def patter_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern)):
        if text[i: i + len(pattern)] == pattern:
            count = count + 1
    return count


def main():
    text = raw_input()
    pattern = raw_input()
    print(patter_count(text, pattern))


main()
