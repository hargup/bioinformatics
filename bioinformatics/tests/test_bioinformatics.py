from bioinformatics import hamming_distance

def test_hamming_distance():
    assert hamming_distance("GGGCCGTTGGT", "GGACCGTTGAC") == 3
