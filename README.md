# Project NIA (Sovereign Logic Engine)

Project NIA is a zero-weight, local-first logic engine designed for autonomous reasoning. It utilizes a 4-language stack to implement the O.D.A. (Observe, Distill, Act) cycle.

## 🚀 Quick Start
```bash
# Initialize environment (requires Ubuntu Noble)
chmod +x setup.sh && ./setup.sh

# Run the engine
python3 main.py
```

## 🏗 Architecture
- **Observe (Python/Playwright)**: Scrapes signals and collects data.
- **Distill (Python/Lua/JS)**:
  - Python: Linguistic Tokenization.
  - Lua: Liquid Time-Constant (LTC) state inference.
  - QuickJS: Semantic Knowledge Mapping.
- **Act (Wren)**: High-speed state machine and reflex execution.

## 📜 Documentation
- [Architecture Details](docs/ARCHITECTURE.md)
- [Technical Requirements](docs/TRD.md)
- [Research Foundations](docs/RESEARCH.md)
- [Changelog](docs/CHANGELOG.md)

## 🔒 License
Proprietary. See [LICENSE](LICENSE) for details.
