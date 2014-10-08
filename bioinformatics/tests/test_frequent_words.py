from bioinformatics.frequent_words import compute_frequencies


def test_compute_frequencies():
    assert compute_frequencies("ATG", 2) == {"AT": 1,
                                             "TG": 1}
