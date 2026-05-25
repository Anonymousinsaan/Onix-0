# Technical Requirements Document (TRD) - Project NIA

## 1. Technical Stack
- **Python (3.10+)**: Responsible for high-level linguistic processing, tokenization, and semantic intent normalization using Porter Stemmer and Synset mapping.
- **Lua (5.4)**: Implements the Liquid Time-Constant (LTC) Engine for continuous-time state inference and fast numerical updates.
- **QuickJS**: Manages the Semantic Knowledge Graph using a directed graph structure for lightweight memory storage.
- **Wren**: Handles the behavioral State Machine and Reflex Cache (CAG layer) for rapid response execution.

## 2. Integration Layer
- **C-FFI / Native Bindings**: Core components are connected via a high-performance C bridge to ensure low-latency communication between different runtimes.
- **Fast-Execution Loop**: A single unified loop orchestrates the O.D.A. cycle across all four languages.

## 3. Data & Memory
- **RAM Limit**: Maximum 1GB resident memory.
- **Persistence**: Local-first storage for the Knowledge Graph and State Trees.
- **Micro-LLM**: Integration with `SmolLM2-135M` in GGUF format for localized generative assistance.

## 4. Automation
- **Playwright**: Headless scraping for live data "scouting" (Observe layer).
