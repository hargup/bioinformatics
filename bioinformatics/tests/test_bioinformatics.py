from bioinformatics import hamming_distance, find_all_approx_occurances


def test_hamming_distance():
    assert hamming_distance("GGGCCGTTGGT", "GGACCGTTGAC") == 3


def test_find_all_approx_occurances():
    text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGG" + \
        "CCTCCACGGTACGGACGTCAATCAAAT"
    pattern = "ATTCTGGA"
    d = 3
    assert find_all_approx_occurances(text, pattern, d) == [6, 7, 26, 27]
