from bioinformatics import (
    hamming_distance, find_all_approx_occurances, count_d,
    frequest_words_with_missmatches, fwmrcp, translate,
    peptide_encoding_problem)


def test_hamming_distance():
    assert hamming_distance("GGGCCGTTGGT", "GGACCGTTGAC") == 3


def test_find_all_approx_occurances():
    text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGG" + \
        "CCTCCACGGTACGGACGTCAATCAAAT"
    pattern = "ATTCTGGA"
    d = 3
    assert find_all_approx_occurances(text, pattern, d) == [6, 7, 26, 27]


def test_count_d():
    assert count_d("AACAAGCTGATAAACATTTAAAGAG", "AAAAA", 1) == 4


def test_frequest_words_with_missmatches():
    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d = 1
    assert frequest_words_with_missmatches(text, k, d) == \
        set(["GATG", "ATGC", "ATGT"])


def test_fwmrcp():
    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d = 1
    assert fwmrcp(text, k, d) == \
        set(["ATGT", "ACAT"])


def test_translate():
    rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    peptide = "MAMAPRTEINSTRING"
    assert translate(rna) == peptide

    rna = "GA"
    assert translate(rna) == ""


def test_peptide_encdoding_problem():
    dna = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
    peptide = "MA"
    encoding_substrings = ["ATGGCC", "GGCCAT", "ATGGCC"]

    assert peptide_encoding_problem(dna, peptide) == encoding_substrings
