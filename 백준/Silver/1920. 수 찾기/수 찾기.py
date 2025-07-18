import sys

def bsearch(n, arr, start, end):

    if start > end:
        return 0

    mid = (start + end) // 2

    if n < arr[mid]:
        return bsearch(n, arr, 0, mid - 1)
    elif n == arr[mid]:
        return 1
    else:
        return bsearch(n, arr, mid + 1, end)


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))

A.sort()

for i in range(M):
    print(bsearch(S[i], A, 0, N - 1))

