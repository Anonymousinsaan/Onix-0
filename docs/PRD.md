# Product Requirements Document (PRD) - Project NIA

## 1. Overview
Project NIA is a Sovereign Logic Engine designed to be zero-weight and zero-training. It operates on the O.D.A. (Observe, Distill, Act) principle to provide autonomous reasoning and action capabilities in a local-first environment.

## 2. Goals
- **Zero-Weight Memory**: Utilize semantic knowledge graphs for efficient state and memory management.
- **Zero-Training Logic**: Use hardcoded and heuristic-based logic engines (LTC, State Machines) instead of large-scale retraining.
- **Multi-Language Sovereignty**: Leverage specialized runtimes (Python, Lua, QuickJS, Wren) for their respective strengths.
- **Privacy & Autonomy**: No external cloud dependencies for core logic or data processing.

## 3. O.D.A. Framework
- **Observe**: Collect raw data and signals via linguistic tokenizers and scrapers.
- **Distill**: Process signals into semantic intents and state inferences using the LTC engine and semantic normalizer.
- **Act**: Execute behavioral state transitions and cached reflexes.

## 4. Constraints
- RAM Ceiling: 1GB.
- Local Inference: Support for SmolLM2-135M GGUF.
- Mobile-First: Optimized for developers using mobile devices (Termux/GitHub).
