from itertools import combinations
*a, = list(map(int,open(0)))

for c in combinations(a,7):
    if sum(c) == 100:
        ls = list(c)
        ls.sort()
        print("\n".join(map(str,ls)))
        break