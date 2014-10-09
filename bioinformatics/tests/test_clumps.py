from bioinformatics.clump import find_clumps
from sympy.utilities.pytest import slow, XFAIL, raises, skip


def test_find_clums_basic():
    text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAG" + \
        "ACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    assert find_clumps(text, 5, 50, 4) == {'CGACA', 'GAAGA'}


def test_find_clumps_intermediate():
    data_file = open('bioinformatics/tests/clump_finding_data.txt', 'r')
    # find a better way to handle the path
    _, text, k, L, t, _, substr = [line[:-1] for line in data_file.readlines()]
    # k = 11
    # L = 566
    # t = 18
    # len(text) = 3869
    k, L, t = int(k), int(L), int(t)

    assert find_clumps(text, k, L, t) == set([substr])


@slow
def test_find_clumps_hard():
    data_file = open('bioinformatics/tests/E-coli.txt', 'r')
    text = data_file.readline()[:-1]

    assert len(find_clumps(text, 9, 500, 3)) == 1904
