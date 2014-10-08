from .frequent_words import frequent_words


def find_clums(text, L, t, k):
    """
    Clump Finding Problem: Find patterns forming clumps in a string.
        Input: A string Genome, and integers k, L, and t.
        Output: All distinct k-mers forming (L, t)-clumps in Genome.

    A k-mer forms a (L, t) clump if in a substring of length L has more than t
    instances of the given k-mer.
    """
    for i in range(len(text) - L + 1):
        substring = text[i: i+L]
    pass
