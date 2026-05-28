import sys
import os

# Add the current directory to sys.path to ensure local imports work
sys.path.append(os.path.dirname(__file__))

from normalizer import SemanticNormalizer
from inference import LLMBridge
from ffi_bridge import send_bridge_message

class NIAOrchestrator:
    """
    Sovereign Logic Engine Orchestrator (Project NIA).
    Coordinates the Observe, Distill, and Act phases.
    """
    def __init__(self):
        print("[NIA] Initializing Engine Components...")
        self.normalizer = SemanticNormalizer()
        self.llm = LLMBridge()
        print("[NIA] Engine Ready.")

    def run_cycle(self, user_input):
        """Executes one O.D.A. cycle."""
        print(f"\n[Observe] Raw Input: '{user_input}'")

        # 1. Distill (Semantic Normalization)
        intents = self.normalizer.distill_intent(user_input)
        print(f"[Distill] Semantic Intents: {intents}")

        # 2. Distill (Cognitive Context)
        llm_prompt = f"Distill the core action from this command: '{user_input}'. Intents identified: {intents}."
        reasoning = self.llm.generate(llm_prompt, max_tokens=64)
        print(f"[Distill] Cognitive Reasoning: {reasoning}")

        # 3. Act (Triggering Lua/Wren via C-FFI)
        print(f"[Act] Executing reflexes for intents {intents}...")
        for intent in intents:
            if intent == "query":
                print(" -> Action: Querying Knowledge Graph (QuickJS)")
                send_bridge_message("JS", "query_graph")
            elif intent == "action":
                print(" -> Action: Updating LTC State (Lua)")
                send_bridge_message("LUA", "update_ltc")
            elif intent == "stop":
                print(" -> Action: Transitioning State Machine to IDLE (Wren)")
                send_bridge_message("WREN", "transition_idle")

        return reasoning

if __name__ == "__main__":
    engine = NIAOrchestrator()

    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = "Please start a search for data updates."

    engine.run_cycle(user_input)
