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


if __name__ == "__main__":
    import sys
    import math
    s = read_fasta_strings(sys.stdin)[0]
    n_A, n_C = s.count('A'), s.count('C')
    print(math.factorial(n_A)*math.factorial(n_C))
