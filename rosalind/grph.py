# Author: Harsh Gupta
# Date: 18th August 2014
# Overlap Graphs http://rosalind.info/problems/grph/

def read_input(in_file):
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


def is_connected(dna_a, dna_b, k=3):
    """
    Inputs two DNAs and retuns if there exists a directed edge betweek
    DNAa and DNAb in an O(k) overlay graph.
    """
    return (dna_a[-k:] == dna_b[:k] and dna_a != dna_b)


def overlay_graph(dna_strings):
    graph = []
    for dna_a in dna_strings.keys():
        for dna_b in dna_strings.keys():
            if is_connected(dna_strings[dna_a], dna_strings[dna_b]):
                graph.append((dna_a, dna_b))
    return graph


def print_output(graph, out_file):
    out_file.writelines(["%s %s\n" % (dna_a, dna_b) for dna_a, dna_b in graph])


if __name__ == "__main__":
    import sys
    dna_strings = read_input(sys.stdin)
    print_output(overlay_graph(dna_strings), sys.stdout)
