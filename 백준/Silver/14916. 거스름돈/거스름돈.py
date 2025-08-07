import sys

input = sys.stdin.readline
# 거스름돈의 액수
N = int(input().rstrip())

INF = int(1e9)
# 동전
coins = [2, 5]

# dp정의
dp = [INF] * (N + 1)
dp[0] = 0
for coin in coins:
    for i in range(coin, N + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
    # print(dp)

print(dp[N]) if dp[N] != INF else print(-1)
