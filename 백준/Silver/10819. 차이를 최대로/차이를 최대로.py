from itertools import permutations
N = int(input())
A = map(int,input().split())

results = []
for x in list(permutations(A,N)):
    max_sum = 0
    for i in range(N-1):
        max_sum += abs(x[i+1] - x[i])
    results.append(max_sum)
print(max(results))
