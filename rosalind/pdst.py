def read_fasta_strings(in_file):
    """ Reads the input and returns a dictionary of DNA inputs """
    tags = []
    strings = []
    for line in in_file.readlines():
        if line[0] == '>':
            tags.append(line[1:-1])
            strings.append('')
        else:
            strings[-1] += line[:-1]
    return strings


def distance(str_a, str_b):
    no_matching_positions = sum([1 for p, q in zip(str_a, str_b) if p != q])
    return no_matching_positions/float(len(str_a))


def calc_distance_matric(strings):
    n = len(strings)
    dist_matrix = [[distance(strings[i], strings[j]) for i in range(n)]
                   for j in range(n)]
    return dist_matrix


if __name__ == "__main__":
    import sys
    dna_strings = read_fasta_strings(sys.stdin)
    dist_matrix = calc_distance_matric(dna_strings)

    n = len(dna_strings)

    for i in range(n):
        out_str = ' '.join([str(x) for x in dist_matrix[i]])
        print(out_str)
