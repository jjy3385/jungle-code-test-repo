import sys

input = sys.stdin.readline
N = int(input().rstrip())
A = [int(input().rstrip()) for _ in range(N)]

top = A[-1]
count = 1
for i in range(N - 2, -1, -1):
    if top < A[i]:
        count += 1
        top = A[i]

print(count)