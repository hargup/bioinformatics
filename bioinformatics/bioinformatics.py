comp_dict = {'A': 'T',
             'T': 'A',
             'G': 'C',
             'C': 'G'}


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


bp_num_dict = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3}

num_bp_dict = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'}


def pattern_to_number(pattern):
    factor = 1
    num = 0
    for bp in pattern[::-1]:
        num = num + factor*bp_num_dict[bp]
        factor = factor * 4
    return num


def number_to_pattern(num, k):
    rev_pattern = ''

    for i in range(k):
        bp = num_bp_dict[num % 4]
        num = num/4
        rev_pattern += bp

    pattern = rev_pattern[::-1]
    return pattern


def computing_frequencies(text, k):
    frequency_array = [0 for i in range(0, pow(4, k))]

    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1

    return frequency_array


def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern)):
        if text[i: i + len(pattern)] == pattern:
            count = count + 1
    return count


def frequent_words(text, k):
    frequenent_patterns = set()
    count = [0 for i in range(0, len(text) - k)]
    for i in range(0, len(text) - k):
        pattern = text[i: i + k]
        count[i] = pattern_count(text, pattern)
        max_count = max(count)

    for i in range(0, len(text) - k):
        if count[i] == max_count:
            frequenent_patterns.add(text[i: i + k])

    return frequenent_patterns


def faster_frequent_words(text, k):
    frequenent_patterns = set()
    frequency_array = computing_frequencies(text, k)
    max_count = max(frequency_array)

    for i in range(0, pow(4, k)):
        if frequency_array[i] == max_count:
            pattern = text[i: i+k]
            frequenent_patterns.add(pattern)

    return frequenent_patterns
