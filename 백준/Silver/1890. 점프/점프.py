
import sys

input = sys.stdin.readline


# 게임판의 크기 (4 <= N <= 100)
N = int(input().rstrip())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        d = board[i][j]
        if d == 0:
            continue

        if i + d < N:
            dp[i + d][j] += dp[i][j]

        if j + d < N:
            dp[i][j + d] += dp[i][j]
            
print(dp[N - 1][N - 1])
