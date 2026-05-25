/**
 * knowledge_graph.js
 * QuickJS Semantic Knowledge Graph (Directed Graph storage).
 */

class KnowledgeGraph {
    constructor() {
        this.nodes = new Map(); // id -> data
        this.edges = [];       // { from, to, type }
    }

    addNode(id, data = {}) {
        if (!this.nodes.has(id)) {
            this.nodes.set(id, data);
        }
        return id;
    }

    addEdge(from, to, type) {
        this.addNode(from);
        this.addNode(to);
        this.edges.push({ from, to, type });
    }

    getRelated(id, type) {
        return this.edges
            .filter(e => e.from === id && (!type || e.type === type))
            .map(e => e.to);
    }

    toJSON() {
        return JSON.stringify({
            nodes: Array.from(this.nodes.entries()),
            edges: this.edges
        });
    }
}

// Example usage
/*
const kg = new KnowledgeGraph();
kg.addEdge("User", "ProjectNIA", "creator");
kg.addEdge("ProjectNIA", "SovereignEngine", "is_a");
console.log(kg.getRelated("ProjectNIA"));
*/

export { KnowledgeGraph };
