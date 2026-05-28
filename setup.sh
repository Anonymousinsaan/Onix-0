# setup.sh - Initialize Project NIA Environment

set -e

echo "Initializing Sovereign Logic Engine (Project NIA)..."

# 1. Update and install runtimes
echo "Installing runtimes (Python, Lua, QuickJS)..."
apt-get update
apt-get install -y python3 python3-pip python3-dev python3-venv lua5.4 quickjs unzip build-essential libffi-dev

# 2. Download Wren CLI (v0.4.0)
echo "Downloading Wren CLI..."
WREN_URL="https://github.com/wren-lang/wren-cli/releases/download/0.4.0/wren-cli-linux-0.4.0.zip"
curl -L $WREN_URL -o wren.zip
unzip -o wren.zip -d bin_wren
mv bin_wren/wren-cli-linux-0.4.0/wren_cli .
rm -rf wren.zip bin_wren

# 3. Setup Python virtual environment & dependencies
echo "Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install llama-cpp-python cffi setuptools

# 4. Download Model
echo "Downloading SmolLM2 model..."
mkdir -p models
MODEL_URL="https://huggingface.co/bartowski/SmolLM2-135M-Instruct-GGUF/resolve/main/SmolLM2-135M-Instruct-Q4_K_M.gguf"
curl -L $MODEL_URL -o models/SmolLM2-135M-Instruct-Q4_K_M.gguf

echo "Environment setup complete."
