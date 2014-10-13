from .bioinformatics import all_kerms_in_text


# There are two approaches, either I can find the all the possible k-mers of
# compute a dictionary of before hand and then update it. The other approach
# is to create a dictionory on the fly. While iterating over the genome
# check if we already have that k-mer in the dictonary if not then add that.
#
# When k is large the initially computed dictionary can be **very** large.
# But when generating the dictionary on the fly is expensive because checking if
# the given k-mer is in the dictionary takes a lot of time.
#
# when k is small the second approach is better but it takes forever for large
# genomes when k is large the first approach takes forever. BTW I think
# can have cheaper on the fly dictionary creation.
# On approach can be iterating over the genome one and find all the kemers
def find_clumps(text, k, L, t):
    """
    Clump Finding Problem: Find patterns forming clumps in a string.
        Input: A string Genome, and integers k, L, and t.
        Output: All distinct k-mers forming (L, t)-clumps in Genome.

    A k-mer forms a (L, t) clump if in a substring of length L has more than t
    instances of the given k-mer.
    """
    valid_k_mers = set()

    # intialize frequencies
    substr_freq = dict([(k_mer, 0) for k_mer in all_kerms_in_text(text, k)])

    # find the frequencies in the first clump
    for i in range(0, L-k+1):
        substr = text[i: i+k]
        substr_freq[substr] += 1

        if substr_freq[substr] >= t:
            valid_k_mers.add(substr)

    for i in range(1, len(text) - L + 1):
        removed_substr = text[i-1: i-1+k]
        added_substr = text[i+L-k: i+L]
        substr_freq[removed_substr] -= 1

        substr_freq[added_substr] += 1

        if substr_freq[added_substr] >= t:
            valid_k_mers.add(added_substr)

    return valid_k_mers
