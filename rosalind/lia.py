import math

def nCr(n, r):
    f = math.factorial
    return f(n)/(f(r)*f(n-r))

def prob(k, n):
    # probablity that at least n organisms will be of type AaBb in a population size of k
    vals_arr = [nCr(k, i)*pow(1/4, i)*pow(3/4, k - i) for i in range(n)]
    res =  1 - sum(vals_arr)
    return res

if __name__ == "__main__":
    import sys
    k, n = [int(x) for x in sys.stdin.readline()[:-1].split(' ')]
    print(prob(pow(2, k), n))
