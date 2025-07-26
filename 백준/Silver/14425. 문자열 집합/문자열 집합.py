import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 집합S
S = [input().rstrip() for _ in range(N)]

# 검사해야할 문자열 A
A = [input().rstrip() for _ in range(M)]

string_set = set(S)

count = 0
for i in range(M):
    if A[i] in string_set:
        count += 1

print(count)
