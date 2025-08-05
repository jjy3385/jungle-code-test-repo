import sys

input = sys.stdin.readline
N = int(input().rstrip())
P = list(map(int, input().rstrip().split()))

P.sort()

temp = 0
total = 0
for i in range(N):
    temp += P[i]
    total += temp
    # print(total)


print(total)