from bioinformatics.protien import (
    calc_mass, calc_linear_spectrum, calc_circular_spectrum)


def test_calc_mass():
    assert calc_mass("VKLFPWFNQY") == 1322


def test_calc_linear_spectrum():
    assert calc_linear_spectrum("NQEL") == \
        [0, 113, 114, 128, 129, 242, 242, 257, 370, 371, 484]


def test_calc_circular_spectrum():
    assert calc_circular_spectrum("NQEL") == \
        [0, 113, 114, 128, 129, 227, 242, 242, 257, 355, 356, 370, 371, 484]
