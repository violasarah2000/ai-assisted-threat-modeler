import matplotlib.pyplot as plt
import networkx as nx

def build_graph(components, flows):
    G = nx.DiGraph()
    for c in components:
        G.add_node(c)
    for src, dst in flows:
        G.add_edge(src, dst)
    return G

def save_graph_png(G, path="diagram.png"):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True, arrowsize=20, node_size=2000, font_size=10)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path
