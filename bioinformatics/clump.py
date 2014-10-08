from .frequent_words import compute_frequencies


def find_clumps(text, k, L, t):
    """
    Clump Finding Problem: Find patterns forming clumps in a string.
        Input: A string Genome, and integers k, L, and t.
        Output: All distinct k-mers forming (L, t)-clumps in Genome.

    A k-mer forms a (L, t) clump if in a substring of length L has more than t
    instances of the given k-mer.
    """
    valid_k_mers = set()
    for i in range(len(text) - L + 1):
        substring = text[i: i+L]
        substr_freq = compute_frequencies(substring, k)
        for substr in substr_freq.keys():
            if substr_freq[substr] >= t:
                valid_k_mers.add(substr)

    return valid_k_mers


# We can use airspeed veclocity for speed benchmarking
