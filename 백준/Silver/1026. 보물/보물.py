import sys

input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int,input().rstrip().split()))
B = list(map(int,input().rstrip().split()))

AA = sorted(A)
BB = sorted(B,reverse=True)

S = 0
for i in range(N):
    S += AA[i] * BB[i]

print(S)