prot = {}
prot["TTT"] = "F"
prot["TTC"] = "F"
prot["TTA"] = "L"
prot["TTG"] = "L"
prot["TCT"] = "S"
prot["TCC"] = "S"
prot["TCA"] = "S"
prot["TCG"] = "S"
prot["TAT"] = "Y"
prot["TAC"] = "Y"
prot["TAA"] = "."
prot["TAG"] = "."
prot["TGT"] = "C"
prot["TGC"] = "C"
prot["TGA"] = "."
prot["TGG"] = "W"
prot["CTT"] = "L"
prot["CTC"] = "L"
prot["CTA"] = "L"
prot["CTG"] = "L"
prot["CCT"] = "P"
prot["CCC"] = "P"
prot["CCA"] = "P"
prot["CCG"] = "P"
prot["CAT"] = "H"
prot["CAC"] = "H"
prot["CAA"] = "Q"
prot["CAG"] = "Q"
prot["CGT"] = "R"
prot["CGC"] = "R"
prot["CGA"] = "R"
prot["CGG"] = "R"
prot["ATT"] = "I"
prot["ATC"] = "I"
prot["ATA"] = "I"
prot["ATG"] = "M"
prot["ACT"] = "T"
prot["ACC"] = "T"
prot["ACA"] = "T"
prot["ACG"] = "T"
prot["AAT"] = "N"
prot["AAC"] = "N"
prot["AAA"] = "K"
prot["AAG"] = "K"
prot["AGT"] = "S"
prot["AGC"] = "S"
prot["AGA"] = "R"
prot["AGG"] = "R"
prot["GTT"] = "V"
prot["GTC"] = "V"
prot["GTA"] = "V"
prot["GTG"] = "V"
prot["GCT"] = "A"
prot["GCC"] = "A"
prot["GCA"] = "A"
prot["GCG"] = "A"
prot["GAT"] = "D"
prot["GAC"] = "D"
prot["GAA"] = "E"
prot["GAG"] = "E"
prot["GGT"] = "G"
prot["GGC"] = "G"
prot["GGA"] = "G"
prot["GGG"] = "G"

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


def transcribed_proteins(rna_str):
    n = len(rna_str)
    proteins = []

    amino_str = ''

    start = False
    for i in range(0, n, 3):
        codon = rna_str[i: i + 3]
        if len(codon) < 3:
            continue
        amino_acid = prot[codon]
        amino_str += amino_acid

    start_pos = amino_str.find('M', 0)
    while start_pos != -1:
        stop_pos = amino_str.find('.', start_pos)
        if stop_pos != -1:
            proteins.append(amino_str[start_pos: stop_pos])
        start_pos += 1
        start_pos = amino_str.find('M', start_pos)

    return proteins


if __name__ == "__main__":
    import sys
    from functools import reduce
    rna_str = read_fasta_strings(sys.stdin)[0]
    orf = all_reading_frames(rna_str)
    proteins = reduce(lambda x, y: x + y, [transcribed_proteins(rf) for rf in orf], [])
    proteins = list(set(proteins))

    for protein in proteins:
        print(protein)
