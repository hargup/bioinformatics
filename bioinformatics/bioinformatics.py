def all_kerms(k):
    from itertools import product
    k_mers = [''.join(bp_tuple) for bp_tuple in product('ATGC', repeat=k)]
    return k_mers


def all_kerms_in_text(text, k):
    k_mers = set()
    for i in range(len(text)-k+1):
        k_mers.add(text[i:i+k])

    return k_mers


def read_fasta_strings(in_file):
    """ Reads the input and returns a dictionary of rna inputs """
    tags = []
    strings = []
    for line in in_file.readlines():
        if line[0] == '>':
            tags.append(line[1:-1])
            strings.append('')
        else:
            strings[-1] += line[:-1]
    return strings


def rev_comp(rna_str):
    comp_dict = {'A': 'T',
                 'T': 'A',
                 'G': 'C',
                 'C': 'G'}

    comp = ''.join([comp_dict[bp] for bp in rna_str])
    return comp[::-1]


def all_reading_frames(rna_str):
    reading_frames = [rna_str, rna_str[1:], rna_str[2:]]
    rna_rev_comp = rev_comp(rna_str)
    reading_frames.append(rna_rev_comp)
    reading_frames.append(rna_rev_comp[1:])
    reading_frames.append(rna_rev_comp[2:])
    return reading_frames


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


def hamming_distance(a, b):
    return sum([1 for p, q in zip(a, b) if p != q])


def find_all_approx_occurances(text, pattern, d):
    """
    Find all starting positions where Pattern appears as a substring of Text
    with at most d mismatches.
    """
    all_occurances = list()
    k = len(pattern)
    n = len(text)

    for i in range(0, n - k + 1):
        if hamming_distance(text[i: i+k], pattern) <= d:
            all_occurances.append(i)

    return all_occurances
