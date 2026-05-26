import subprocess
import json
import os

class NIABridge:
    """
    NIABridge orchestrates the multi-language execution loop.
    It manages communication between Python and the specialized VMs (Lua, QuickJS, Wren).
    """

    def __init__(self, root_dir="."):
        self.root_dir = root_dir
        self.wren_bin = os.path.join(root_dir, "wren_cli")

    def run_lua(self, input_vector, dt=0.1):
        """Runs the LTC Engine in Lua."""
        script = os.path.join(self.root_dir, "core/logic_lua/ltc_engine.lua")
        # Wrapper to pass inputs and get state
        cmd = [
            "lua5.4", "-e",
            f"local ltc = require('core.logic_lua.ltc_engine'); "
            f"local engine = ltc.new({len(input_vector)}, 0.5); "
            f"engine:update({{{','.join(map(str, input_vector))}}}, {dt}); "
            f"print(table.concat(engine:get_state(), ','))"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            return None
        return [float(x) for x in result.stdout.strip().split(',')]

    def run_js(self, action, data):
        """Runs the Knowledge Graph in QuickJS."""
        script = os.path.join(self.root_dir, "core/graph_js/knowledge_graph.js")
        # Temporary runner for JS
        js_code = f"""
        import {{ KnowledgeGraph }} from '{script}';
        const kg = new KnowledgeGraph();
        {f'kg.addEdge("{data["from"]}", "{data["to"]}", "{data["type"]}");' if action == 'add' else ''}
        console.log(kg.toJSON());
        """
        with open("temp_kg.js", "w") as f:
            f.write(js_code)

        result = subprocess.run(["qjs", "temp_kg.js"], capture_output=True, text=True)
        os.remove("temp_kg.js")
        if result.returncode != 0:
            return None
        return json.loads(result.stdout.strip())

    def run_wren(self, state_transition):
        """Runs the Reflex Cache in Wren."""
        script = os.path.join(self.root_dir, "core/state_wren/reflex_cache.wren")
        wren_code = f"""
        import "{os.path.join(self.root_dir, "core/state_wren/reflex_cache")}" for ReflexCache
        var cache = ReflexCache.new()
        cache.addState("idle") {{ System.print("idle") }}
        cache.addState("acting") {{ System.print("acting") }}
        cache.transition("{state_transition}")
        cache.execute()
        """
        with open("temp_reflex.wren", "w") as f:
            f.write(wren_code)

        result = subprocess.run([self.wren_bin, "temp_reflex.wren"], capture_output=True, text=True)
        os.remove("temp_reflex.wren")
        return result.stdout.strip()

if __name__ == "__main__":
    bridge = NIABridge()
    print("Testing Lua LTC:", bridge.run_lua([1.0, 0.5]))
    print("Testing JS KG:", bridge.run_js("add", {"from": "A", "to": "B", "type": "rel"}))
    print("Testing Wren Reflex:", bridge.run_wren("acting"))
