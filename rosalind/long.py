# Author: Harsh Gupta
# Date: 18th August 2014
# Genome Assembly as Shortest Superstring http://rosalind.info/problems/long/

# The problem is same as finding the hamiltonian path in the overlay graph
# which produces the shortest DNA

import networkx as nx

def read_fasta(in_file):
    """ Reads the input and returns a dictionary of DNA inputs """
    tags = []
    strings = []
    for line in in_file.readlines():
        if line[0] == '>':
            tags.append(line[1:-1])
            strings.append('')
        else:
            strings[-1] += line[:-1]

    return dict(zip(tags, strings))


def overlay(dna_a, dna_b):
    if dna_a == dna_b:
        return (False, 0)

    max_overlap_len = min(len(dna_a), len(dna_b))
    for k in range(max_overlap_len, int(max_overlap_len/2), -1):
        if dna_a[-k:] == dna_b[:k]:
            return (True, k)

    return (False, 0)


def overlay_graph(dna_strings):
    """
    Input
    ----
    dna_strings: dictionary of fasta tags to dna strings

    Output
    -----
    A directed neworkx graph
    """

    DG = nx.DiGraph()
    for tag_a in dna_strings.keys():
        for tag_b in dna_strings.keys():
            is_connected, length = overlay(dna_strings[tag_a], dna_strings[tag_b])
            if is_connected:
                DG.add_edge(tag_a, tag_b, k=length)
    return DG


def hamiltonian_paths(DG):
    n = len(DG.nodes())
    possible_hamiltonian_paths = []
    for node_a in DG.nodes():
        for node_b in DG.nodes():
            paths = nx.all_simple_paths(DG, node_a, node_b)
            possible_hamiltonian_paths += [path for path in paths if len(path) == n]
    return possible_hamiltonian_paths


def find_superstring(dna_strings):
    DG = overlay_graph(dna_strings)
    paths = hamiltonian_paths(DG)
    if len(paths) > 1:
        raise NotImplementedError
    else:
        path = paths[0]
        superstring = dna_strings[path[0]]
        for i in range(1, len(DG.nodes())):
            overlap_len = DG.edge[path[i-1]][path[i]]['k']
            superstring += dna_strings[path[i]][overlap_len:]
        return superstring


def print_output(graph, out_file):
    out_file.writelines(["%s %s\n" % (dna_a, dna_b) for dna_a, dna_b in graph])


import sys
print(find_superstring(read_fasta(sys.stdin)))
