codons = ['F', 'F', 'L', 'L', 'S', 'S', 'S', 'S', 'Y', 'Y', 'C', 'C', 'W',
              'L', 'L', 'L', 'L', 'P', 'P', 'P', 'P', 'H', 'H', 'Q', 'Q', 'R',
              'R', 'R', 'R', 'I', 'I', 'I', 'M', 'T', 'T', 'T', 'T', 'N', 'N',
              'K', 'K', 'S', 'S', 'R', 'R', 'V', 'V', 'V', 'V', 'A', 'A', 'A',
              'A', 'D', 'D', 'E', 'E', 'G', 'G', 'G', 'G', 'Stop', 'Stop', 'Stop']

codon_freq = {}
for codon in codons:
    if codon in codon_freq.keys():
        codon_freq[codon] += 1
    else:
        codon_freq[codon] = 1

import sys
rna = sys.stdin.readline()[:-1]
big_num = 1000000
possible_rnas = reduce(lambda x, y: (x*y)%big_num,
                       [codon_freq[codon] for codon in rna], 3) # initial three for 3 stop codons
print(possible_rnas)
