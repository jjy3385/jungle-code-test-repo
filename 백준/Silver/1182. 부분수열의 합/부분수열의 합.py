from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(1, N + 1):
    for c in list(combinations(nums, i)):
        if sum(c) == S:
            count += 1
print(count)