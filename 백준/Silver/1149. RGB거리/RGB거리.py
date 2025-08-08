import sys

input = sys.stdin.readline

# N개의 집
N = int(input().rstrip())
costs = [list(map(int, input().rstrip().split())) for _ in range(N)]

INF = int(1e9)


dp = [[0] * 3 for _ in range(N)]
dp[0] = costs[0]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]


print(min(dp[N - 1]))
