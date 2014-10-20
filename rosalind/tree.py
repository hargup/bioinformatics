import networkx as nx

def read_graph(in_file):
    n = int(in_file.readline())
    G = nx.Graph()
    for i in range(1, n+1): G.add_node(i)

    for line in in_file.readlines():
        u, v = [int(x) for x in line.split(' ')]
        G.add_edge(u, v)
    return G

if __name__ == "__main__":
    import sys
    G = read_graph(sys.stdin)
    print(nx.number_connected_components(G) - 1)
