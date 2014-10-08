def count_occurances(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            count = count + 1
    return count


def frequent_words(text, k):
    """
    find the most frequent k-mers in the text
    """
    frequenent_patterns = set()
    count = [0 for i in range(0, len(text) - k + 1)]
    for i in range(0, len(text) - k + 1):
        pattern = text[i: i + k]
        count[i] = count_occurances(text, pattern)
        max_count = max(count)

    for i in range(0, len(text) - k + 1):
        if count[i] == max_count:
            frequenent_patterns.add(text[i: i + k])

    return frequenent_patterns


def faster_frequent_words(text, k):
    frequenent_patterns = set()
    frequency_array = computing_frequencies(text, k)
    max_count = max(frequency_array)

    for i in range(0, pow(4, k)):
        if frequency_array[i] == max_count:
            pattern = text[i: i+k]
            frequenent_patterns.add(pattern)

    return frequenent_patterns


def find_all_occurances(text, pattern):
    all_occurances = list()
    k = len(pattern)
    n = len(text)

    for i in range(0, n - k + 1):
        if text[i: i+k] == pattern:
            all_occurances.append(i)

    return all_occurances


def compute_frequencies(text, k):
    """
    compute frequencies of all k-mers in the text
    """
    frequency_dict = dict()

    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        if pattern in frequency_dict.keys():
            frequency_dict[pattern] += 1
        else:
            frequency_dict[pattern] = 1

    return frequency_dict


bp_num_dict = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3}

num_bp_dict = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'}


def pattern_to_number(pattern):
    factor = 1
    num = 0
    for bp in pattern[::-1]:
        num = num + factor*bp_num_dict[bp]
        factor = factor * 4
    return num


def number_to_pattern(num, k):
    rev_pattern = ''

    for i in range(k):
        bp = num_bp_dict[num % 4]
        num = num/4
        rev_pattern += bp

    pattern = rev_pattern[::-1]
    return pattern
