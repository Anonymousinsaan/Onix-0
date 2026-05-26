# ARCHITECTURE.md - Project NIA

## System Overview
Project NIA is a distributed logic engine where each component is optimized for a specific phase of the O.D.A. cycle.

```mermaid
graph TD
    A[Observation Layer] -->|Raw Text| B(Python: Semantic Normalizer)
    A -->|Live Signals| C(Lua: LTC Engine)
    B -->|Intent| D(QuickJS: Knowledge Graph)
    C -->|State Inference| D
    D -->|Context| E(Wren: State Machine)
    E -->|Reflex| F[Action Layer]
```

## Component Breakdown

### 1. Observation Layer (Python)
- **Location**: `/automation/scout.py`
- **Role**: Uses Playwright for headless data collection.

### 2. Linguistic Tokenizer (Python)
- **Location**: `/bridge/normalizer.py`
- **Role**: Normalizes user input into a canonical semantic form.

### 3. LTC Engine (Lua)
- **Location**: `/core/logic_lua/ltc_engine.lua`
- **Role**: Continuous-time state inference using Liquid Time-Constant dynamics.

### 4. Knowledge Graph (QuickJS)
- **Location**: `/core/graph_js/knowledge_graph.js`
- **Role**: Storing relationships and facts in a zero-weight directed graph.

### 5. Reflex Cache (Wren)
- **Location**: `/core/state_wren/reflex_cache.wren`
- **Role**: High-speed behavioral response and state management.

## Integration Bridge
The components are orchestrated via `bridge/nia_bridge.py`, which manages the communication between Python and the respective VMs (Lua, QJS, Wren).
