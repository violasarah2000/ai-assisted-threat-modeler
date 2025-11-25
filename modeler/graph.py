import os
import networkx as nx
import matplotlib.pyplot as plt

def build_graph(components, flows):
    """
    Build a directed graph from system components and data flows.
    """
    G = nx.DiGraph()

    # Add components as nodes
    for c in components:
        G.add_node(c)

    # Add flows as edges
    for src, dst in flows:
        G.add_edge(src, dst)

    return G


def save_graph_png(G, path="artifacts/diagrams/diagram.png"):
    """
    Saves the system architecture graph to a PNG file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3000,
        node_color="#90caf9",
        font_size=9,
        arrowsize=20,
        edge_color="#555"
    )

    plt.tight_layout()
    plt.savefig(path)
    plt.close()

    return path
