from llama_cpp import Llama
import os

class LLMBridge:
    """
    Bridge for local LLM inference using SmolLM2-135M GGUF.
    Optimized for low RAM footprint.
    """
    def __init__(self, model_path=None):
        if model_path is None:
            model_path = os.path.join(os.path.dirname(__file__), "../models/SmolLM2-135M-Instruct-Q4_K_M.gguf")

        # Initialize Llama model
        # n_ctx: context window size
        # n_threads: number of CPU threads to use
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=2,
            verbose=False
        )

    def generate(self, prompt, max_tokens=128):
        """Generates a response from the model."""
        formatted_prompt = f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"

        output = self.llm(
            formatted_prompt,
            max_tokens=max_tokens,
            stop=["<|im_end|>"],
            echo=False
        )

        return output["choices"][0]["text"].strip()

if __name__ == "__main__":
    bridge = LLMBridge()
    test_prompt = "What is the O.D.A. principle in simple terms?"
    print(f"Prompt: {test_prompt}")
    print(f"Response: {bridge.generate(test_prompt)}")
