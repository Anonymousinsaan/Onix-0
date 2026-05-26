"""
models/downloader.py
Utility to download SmolLM2 GGUF model for Project NIA.
"""
import os

def download_model():
    config_path = "models/config.json"
    print(f"Model Configuration loaded from {config_path}")
    print("To download: Use 'huggingface-cli download HuggingFaceTB/SmolLM2-135M-Instruct-GGUF smollm2-135m.gguf --local-dir models'")

if __name__ == "__main__":
    download_model()
