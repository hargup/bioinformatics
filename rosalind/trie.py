import networkx as nx
from matplotlib import pyplot as plt

def create_trie(strings):
    G = nx.Graph()
    G.add_node(1)
    highest_node = 1
    for string in strings:
        root_node = 1
        for char in string:
            adjacent_edges = edge_lables_dict(G, root_node)
            if char in adjacent_edges.keys():
                root_node = adjacent_edges[char]
            else:
                G.add_edge(root_node, highest_node + 1, name=char)
                highest_node += 1
                root_node = highest_node
    return G


def edge_lables_dict(G, node):
    """
    Returns a dict of edges adjacent to node
    where the keys are the edge attribute and values
    are neighbour node
    """
    res_dict = {}
    for neighbor in G.neighbors(node):
        label = G[node][neighbor]["name"]
        if label in res_dict.keys():
            print("node: %s label: %s"%(node, label))
            print(res_dict)
            raise ValueError("The tree is not a valid" \
                             "trie")
        else:
            res_dict[label] = neighbor
    return res_dict


def print_adjacency_list(G):
    for u, v in G.edges():
        print("%s %s %s" % (u, v, G[u][v]["name"]))


if __name__ == "__main__":
    import sys
    strings = [line[:-1] for line in sys.stdin.readlines()]
    G = create_trie(strings)
    print_adjacency_list(G)
