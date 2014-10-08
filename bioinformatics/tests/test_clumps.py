from bioinformatics.clump import find_clumps


def test_find_clums():
    text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAG" + \
        "ACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    assert find_clumps(text, 5, 50, 4) == {'CGACA', 'GAAGA'}

    data_file = open('bioinformatics/tests/clump_finding_data.txt', 'r')
    # find a better way to handle the path
    _, text, k, L, t, _, substr = [line[:-1] for line in data_file.readlines()]
    k, L, t = int(k), int(L), int(t)

    assert find_clumps(text, k, L, t) == set([substr])
