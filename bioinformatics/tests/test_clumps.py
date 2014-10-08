from bioinformatics.clump import find_clumps


def test_find_clums():
    text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAG" + \
        "ACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    assert find_clumps(text, 5, 50, 4) == {'CGACA', 'GAAGA'}
