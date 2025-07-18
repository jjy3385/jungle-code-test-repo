import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

min_h = 0
max_h = max(A)
res = 0

while min_h <= max_h:

    mid_h = (min_h + max_h) // 2

    sum_h = sum(a - mid_h for a in A if a > mid_h)

    if sum_h >= M:
        res = mid_h
        min_h = mid_h + 1
    else:
        max_h = mid_h - 1

print(res)