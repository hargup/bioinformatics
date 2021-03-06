neucleotides = ['A', 'T', 'G', 'C']

translation_dict = {
    "AAA": "K",
    "AAC": "N",
    "AAG": "K",
    "AAU": "N",
    "ACA": "T",
    "ACC": "T",
    "ACG": "T",
    "ACU": "T",
    "AGA": "R",
    "AGC": "S",
    "AGG": "R",
    "AGU": "S",
    "AUA": "I",
    "AUC": "I",
    "AUG": "M",
    "AUU": "I",
    "CAA": "Q",
    "CAC": "H",
    "CAG": "Q",
    "CAU": "H",
    "CCA": "P",
    "CCC": "P",
    "CCG": "P",
    "CCU": "P",
    "CGA": "R",
    "CGC": "R",
    "CGG": "R",
    "CGU": "R",
    "CUA": "L",
    "CUC": "L",
    "CUG": "L",
    "CUU": "L",
    "GAA": "E",
    "GAC": "D",
    "GAG": "E",
    "GAU": "D",
    "GCA": "A",
    "GCC": "A",
    "GCG": "A",
    "GCU": "A",
    "GGA": "G",
    "GGC": "G",
    "GGG": "G",
    "GGU": "G",
    "GUA": "V",
    "GUC": "V",
    "GUG": "V",
    "GUU": "V",
    "UAA": "*",
    "UAC": "Y",
    "UAG": "*",
    "UAU": "Y",
    "UCA": "S",
    "UCC": "S",
    "UCG": "S",
    "UCU": "S",
    "UGA": "*",
    "UGC": "C",
    "UGG": "W",
    "UGU": "C",
    "UUA": "L",
    "UUC": "F",
    "UUG": "L",
    "UUU": "F"}


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


def rev_comp_dna(dna_str):
    comp_dict = {'A': 'T',
                 'T': 'A',
                 'G': 'C',
                 'C': 'G'}

    comp = ''.join([comp_dict[bp] for bp in dna_str])
    return comp[::-1]


def rev_comp_rna(rna_str):
    comp_dict = {'A': 'U',
                 'U': 'A',
                 'G': 'C',
                 'C': 'G'}

    comp = ''.join([comp_dict[bp] for bp in rna_str])
    return comp[::-1]


def all_reading_frames(rna_str):
    reading_frames = [rna_str, rna_str[1:], rna_str[2:]]
    rna_rev_comp = rev_comp_rna(rna_str)
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


def count_d(text, pattern, d):
    """
    We define count_d(text, pattern) as the total number of occurrences
    of Pattern in Text with at most d mismatches.
    """
    return len(find_all_approx_occurances(text, pattern, d))


def frequest_words_with_missmatches(text, k, d):
    possible_k_mers = []
    for i in range(len(text)-k+1):
        possible_k_mers += d_distance_apart(text[i: i+k], d)
    possible_k_mers = list(set(possible_k_mers))

    substr_freq = dict([(k_mer, 0) for k_mer in possible_k_mers])

    for i in range(len(text)-k+1):
        for k_mer in d_distance_apart(text[i: i+k], d):
            substr_freq[k_mer] += 1

    max_freq = max(substr_freq.values())
    frequent_words = [k_mer for k_mer in substr_freq.keys()
                      if substr_freq[k_mer] == max_freq]
    return set(frequent_words)

# There is a lot of code dublication between this function and the above one
# I can rewrite the both of them as a special case of generalised function.


def fwmrcp(text, k, d):
    """
    Frequent Words with Mismatches and Reverse Complements Problem

    Find the most frequent k-mers (with mismatches and reverse complements) in
    a DNA string.
    """
    possible_k_mers = []
    for i in range(len(text)-k+1):
        possible_k_mers += d_distance_apart(text[i: i+k], d)
        possible_k_mers += d_distance_apart(rev_comp_dna(text[i: i+k]), d)
    possible_k_mers = list(set(possible_k_mers))

    substr_freq = dict([(k_mer, 0) for k_mer in possible_k_mers])

    for i in range(len(text)-k+1):
        for k_mer in d_distance_apart(text[i: i+k], d):
            substr_freq[k_mer] += 1

        for k_mer in d_distance_apart(rev_comp_dna(text[i: i+k]), d):
            substr_freq[k_mer] += 1

    max_freq = max(substr_freq.values())
    frequent_words = [k_mer for k_mer in substr_freq.keys()
                      if substr_freq[k_mer] == max_freq]
    return set(frequent_words)


def d_distance_apart(text, d):
    """
    Returns a list of all DNA strings which have a hamming distance of d
    or less with the given string.
    """
    if d == 0:
        return [text]
    elif len(text) == 0:
        return []
    else:
        str_list = [text[0] + tail for tail in d_distance_apart(text[1:], d)] + \
            [bp + tail for tail in d_distance_apart(text[1:], d - 1)
             for bp in set(neucleotides) - set([text[0]])] + \
            [bp + text[1:] for bp in neucleotides]
        return list(set(str_list))


def translate(rna):
    """
    Translates the RNA strign to peptide
    """
    peptide = "".join([translation_dict[rna[i: i+3]]
                       for i in range(0, len(rna), 3) if i+3 <= len(rna)])
    try:
        return peptide[:peptide.index("*")]
    except ValueError:
        return peptide


def peptide_encoding_problem(dna, peptide):
    """
    Finds substrings of a genome encoding a given amino acid sequence.
    """
    seq_len = len(peptide)*3
    encoding_substrings = []
    for i in range(len(dna) - seq_len + 1):
        substr = dna[i:i+seq_len]
        rna_substr = substr.replace('T', 'U')
        if translate(rna_substr) == peptide:
            encoding_substrings.append(substr)

        if translate(rev_comp_rna(rna_substr)) == peptide:
            encoding_substrings.append(substr)

    return encoding_substrings
