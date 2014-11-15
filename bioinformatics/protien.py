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

# doesn't contain Q and L
unique_mass_aa = {"G", "A", "S", "P", "V", "T", "C", "I", "N", "D",
                  "K", "E", "M", "H", "F", "R", "Y", "W"}


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
    prefix_mass = [0]
    k = 0
    for aa in peptide:
        prefix_mass.append(prefix_mass[k] + mass_table[aa])
        k += 1

    peptide_mass = calc_mass(peptide)

    cyclic_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide) + 1):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                cyclic_spectrum.append(peptide_mass -
                                       (prefix_mass[j] - prefix_mass[i]))

    cyclic_spectrum.sort()
    return cyclic_spectrum


def coin_change(coin_list, n):
    m = len(coin_list)
    table = [0 for i in range(n+1)]
    table[0] = 1

    for i in range(0, m):
        for j in range(coin_list[i], n+1):
            table[j] += table[j - coin_list[i]]

    return table[n]


def parent_mass(spectrum):
    return spectrum[-1]


def num_peptide_of_mass(mass):
    mass_list = list(set(mass_table.values()))
    return coin_change(mass_list, mass)


def expand_peptide(peptide):
    """Return k+1 lenght peptides from peptide of length k"""
    k_1_peptides = [peptide + aa for aa in unique_mass_aa]
    return k_1_peptides


def is_subsequence(small_itr, large_itr):
    i, j = 0, 0
    while i < len(small_itr) and j < len(large_itr):
        if small_itr[i] == large_itr[j]:
            i += 1
        j += 1
    return i == len(small_itr)


def is_consistent(peptide, spectrum):
    """
    This problem is as the problem of testing if spectrum
    of peptide is a subsequence of spectrum
    """
    return is_subsequence(calc_linear_spectrum(peptide), spectrum)


def cyclopeptide_sequencing(spectrum):
    peptides = [""]
    results = []
    while len(peptides) > 0:
        peptides = [k_1_peptide for peptide in peptides
                    for k_1_peptide in expand_peptide(peptide)]
        for peptide in peptides:
            if calc_mass(peptide) == parent_mass(spectrum):
                if calc_circular_spectrum(peptide) == spectrum:
                    results.append(peptide)

        peptides = [peptide for peptide in peptides
                    if not calc_mass(peptide) == parent_mass(peptide)]

        peptides = [peptide for peptide in peptides
                    if is_consistent(peptide, spectrum)]

    return results


def format_peptide_mass(peptide):
    out_str = ""
    for aa in peptide[:-1]:
        out_str += str(mass_table[aa]) + "-"

    out_str += str(mass_table[peptide[-1]])
    return out_str
