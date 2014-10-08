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
    substring = text[:L]
    substr_freq = compute_frequencies(substring, k)
    for substr in substr_freq.keys():
        if substr_freq[substr] >= t:
            valid_k_mers.add(substr)

    for i in range(1, len(text) - L + 1):
        removed_substr = text[i-1: i-1+k]
        added_substr = text[i+L-k: i+L]
        substr_freq[removed_substr] -= 1

        if added_substr in substr_freq.keys():
            substr_freq[added_substr] += 1
        else:
            substr_freq[added_substr] = 1

        for substr in substr_freq.keys():
            if substr_freq[substr] >= t:
                valid_k_mers.add(substr)


    return valid_k_mers


# We can use airspeed veclocity for speed benchmarking
