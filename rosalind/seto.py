if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline()[:-1])
    A = set([int(x) for x in sys.stdin.readline()[1:-2].split(', ')])
    B = set([int(x) for x in sys.stdin.readline()[1:-2].split(', ')])
    U = set(list(range(1, n + 1)))
    print(A.union(B))
    print(A.intersection(B))
    print(A - B)
    print(B - A)
    print(U - A)
    print(U - B)
