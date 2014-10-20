# no of unrooted internal node = no of rooted internal nodes - 1

def rin(n): # rooted internal nodes
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return n//2 + rin(n//2 + n%2)


def uin(n):
    return rin(n) - 1

if __name__ == "__main__":
    n = int(input())
    print(uin(n))
