mass_table = {
    "G": 57,
    "A": 71,
    "S": 87,
    "P": 97,
    "V": 99,
    "T": 101,
    "C": 103,
    "I": 113,
    "L": 113,
    "N": 114,
    "D": 115,
    "K": 128,
    "Q": 128,
    "E": 129,
    "M": 131,
    "H": 137,
    "F": 147,
    "R": 156,
    "Y": 163,
    "W": 186}


def calc_mass(peptide):
    return sum([mass_table[aa] for aa in peptide])

def calc_circular_subpeptides(peptide):
    subpeptides = []
    n = len(peptide)
    peptide = peptide + peptide
    # Taking the double lenght so that indexes doens't overflow
    for len_peptide in range(1, n):
        for start_pos in range(n):
            subpeptides.append(peptide[start_pos: start_pos + len_peptide])

    return subpeptides


def calc_linear_spectrum(peptide):
    prefix_mass = [0]
    k = 0
    for aa in peptide:
        prefix_mass.append(prefix_mass[k] + mass_table[aa])
        k += 1

    linear_spectrum = [prefix_mass[j] - prefix_mass[i]
                       for i in range(len(peptide))
                       for j in range(i + 1, len(peptide) + 1)]
    linear_spectrum.append(0)
    linear_spectrum.sort()
    return linear_spectrum


def calc_circular_spectrum(peptide):
    subpeptides = [''] + calc_circular_subpeptides(peptide) + [peptide]
    spectrum = [calc_mass(subpeptide) for subpeptide in subpeptides]
    spectrum.sort()

    return spectrum
