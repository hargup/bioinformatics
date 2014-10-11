def skew(text):
    val = 0
    yield val
    for bp in text:
        if bp == 'G':
            val += 1
        elif bp == 'C':
            val -= 1

        yield val


def min_skew(text):
    """
    Find a positions in a genome minimizing the skew.
    """
    skew_list = list(skew(text))
    min_skew = min(skew_list)
    min_pos = []
    try:
        i = skew_list.index(min_skew)
        min_pos.append(i)
        while True:
            i = skew_list.index(min_skew, i+1)
            min_pos.append(i)
    except ValueError:
        return min_pos
