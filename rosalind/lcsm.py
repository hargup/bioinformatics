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


def longest_common_substrings(strings):
    str_a = strings[0]
    n = len(str_a)
    max_len = 0
    max_sub_str = ''
    for p in range(n):
        for q in range(n, p, -1):
            if all([string.find(str_a[p: q]) != -1 for string in strings]):
                if (q - p) > max_len:
                    max_len = (p - p)
                    max_sub_str = str_a[p: q]
    return max_sub_str


def main():
    import sys
    strings = read_fasta_strings(sys.stdin)
    sub_str = longest_common_substrings(strings)
    print(sub_str)


if __name__ == "__main__":
    main()
