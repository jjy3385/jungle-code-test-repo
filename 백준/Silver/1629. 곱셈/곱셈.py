import sys

input = sys.stdin.readline
A, B, C = map(int, input().rstrip().split())

def multi(a, b, c):

    # base case
    if b == 1:
        return a % c

    half = multi(a, b // 2, c)

    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c


print(multi(A, B, C))
