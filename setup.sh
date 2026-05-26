#!/bin/bash
# setup.sh - Initialize Project NIA Environment

set -e

echo "Initializing Sovereign Logic Engine (Project NIA)..."

# 1. Update and install runtimes
echo "Installing runtimes (Python, Lua, QuickJS)..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip lua5.4 quickjs

# 2. Download Wren CLI (v0.4.0)
echo "Downloading Wren CLI..."
WREN_URL="https://github.com/wren-lang/wren-cli/releases/download/0.4.0/wren-cli-linux-0.4.0.zip"
curl -L $WREN_URL -o wren.zip
unzip -o wren.zip -d bin_wren
mv bin_wren/wren-cli-linux-0.4.0/wren_cli .
rm -rf wren.zip bin_wren

# 3. Setup Python virtual environment
echo "Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
# pip install playwright # Uncomment if needed for automation layer

echo "Environment setup complete."
echo "Check your runtimes:"
python3 --version
lua5.4 -v
qjs -h | head -n 1
./wren_cli -v
