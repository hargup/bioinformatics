from functools import reduce
n, k = [int(x) for x in input().split(' ')]
big_num = 1000000
pnk = reduce(lambda x, y: (x*y)%big_num, [n - i for i in range(k)], 1)
print(pnk)
