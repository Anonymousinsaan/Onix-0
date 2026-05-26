"""
main.py - Project NIA (Sovereign Logic Engine)
Unified O.D.A. Framework Orchestrator.
"""

import time
import sys
from bridge.normalizer import SemanticNormalizer
from bridge.nia_bridge import NIABridge

def main():
    print("--- Project NIA Sovereign Logic Engine ---")
    print("--- Cycle: Observe -> Distill -> Act ---")

    normalizer = SemanticNormalizer()
    bridge = NIABridge()

    # Simulation of O.D.A. Cycle
    while True:
        try:
            # 1. OBSERVE (User Input or Scout)
            raw_input = input("\n[OBSERVE] > ")
            if raw_input.lower() in ["exit", "quit"]:
                break

            # 2. DISTILL
            # a) Linguistic
            intents = normalizer.distill_intent(raw_input)
            print(f"[DISTILL] Intents: {intents}")

            # b) State Inference (LTC)
            # Map input to a simple vector for simulation
            input_vector = [1.0 if i in intents else 0.0 for i in ["query", "action", "stop"]]
            ltc_state = bridge.run_lua(input_vector)
            print(f"[DISTILL] LTC State: {ltc_state}")

            # c) Knowledge Mapping (KG)
            if intents:
                kg_update = bridge.run_js("add", {"from": "User", "to": intents[0], "type": "intent"})
                print(f"[DISTILL] KG Updated: {len(kg_update['nodes'])} nodes")

            # 3. ACT
            transition = "acting" if "action" in intents or "query" in intents else "idle"
            reflex = bridge.run_wren(transition)
            print(f"[ACT] Reflex: {reflex.splitlines()[-1]}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

    print("\nProject NIA: Hibernating.")

if __name__ == "__main__":
    main()
