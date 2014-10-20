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

comp_dict = {'A': 'T',
             'T': 'A',
             'G': 'C',
             'C': 'G'}


def remove_dublicates(l):
    """ returns a set of the elements in l which doesn't occur twice """
    single_occurance = set()
    for elem in l:
        if elem in single_occurance or elem[::-1] in single_occurance:
            single_occurance.remove(elem)
        else:
            single_occurance.add(elem)
    return single_occurance


def corrections(single_occurance):
    corr_dict = dict()
    added_values = set()
    for p in single_occurance:
        for q in single_occurance:
            if hamming_distance(p, q) == 1:
                if not p in added_values and not q in added_values:
                    corr_dict[p] = q
                    added_values.add(p)
                    added_values.add(q)
            elif hamming_distance(p, rev_comp(q)) == 1:
                q = rev_comp(q)
                if not p in added_values and not q in added_values:
                    corr_dict[p] = q
                    added_values.add(p)
                    added_values.add(q)
    print("added_values", added_values)

    return corr_dict


if __name__ == "__main__":
    import sys
    strings = read_fasta_strings(sys.stdin)
    single_occurance = remove_dublicates(strings)
    print(single_occurance)
    corr_dict = corrections(single_occurance)
    print(corr_dict)
    for dna in corr_dict:
        print("%s->%s" % (dna, corr_dict[dna]))
