# RESEARCH.md - Theoretical Foundations of Project NIA

Project NIA is built upon several key academic and technical pillars.

## 1. Liquid Time-Constant (LTC) Networks
Project NIA utilizes LTCs for continuous-time state inference. Unlike traditional RNNs, LTCs are inspired by the nervous system of small organisms (like C. elegans) and are defined by differential equations.
- **Reference**: Hasani, R., et al. "Liquid Time-constant Networks." *Nature Machine Intelligence*, 2021.
- **Application**: Located in `core/logic_lua/ltc_engine.lua`.

## 2. O.D.A. (Observe, Distill, Act) Framework
A simplified loop for autonomous reasoning, derived from the OODA loop (Observe, Orient, Decide, Act) developed by military strategist John Boyd.
- **Observe**: Data collection (Automation/Playwright).
- **Distill**: Semantic normalization and state inference (Python/Lua/JS).
- **Act**: Execution of behavioral reflexes (Wren).

## 3. Semantic Knowledge Graphs
Zero-weight memory storage using directed graphs to map relationships without the overhead of heavy vector databases.
- **Concept**: Semantic Web and Knowledge Representation.
- **Application**: Located in `core/graph_js/knowledge_graph.js`.

## 4. Multi-VM Orchestration
The use of specialized virtual machines (Lua, QuickJS, Wren) coordinated by a Python bridge ensures memory efficiency and high-speed execution within a 1GB RAM ceiling.
