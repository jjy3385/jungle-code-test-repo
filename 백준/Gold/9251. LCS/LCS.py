import sys

input = sys.stdin.readline

str_A = input().rstrip()
str_B = input().rstrip()
N = len(str_A)
M = len(str_B)

LCS = [[0] * (M + 1) for _ in range(N + 1)]


for i in range(N + 1):
    for j in range(M + 1):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif str_A[i - 1] == str_B[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

            
print(LCS[N][M])