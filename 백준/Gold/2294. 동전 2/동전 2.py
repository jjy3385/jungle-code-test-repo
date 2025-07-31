import sys

input = sys.stdin.readline

# 가치의 합이 K
N, K = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(N)]

# 사용한 동전의 최소개수를 구하라
# dp라고하는데 어떻게 접근해야될지조차 잘 모르겠군
# 구하는것이 최소 동전의 갯수
INF = 1e9

# 이 배열이 요소가 의미하는 것
# dp[1] -> 1원을 만드는 최소 동전의 갯수
# dp[2] -> 2원을 만드는 최소 동전의 갯수
# ...
# dp[k] -> k원을 만드는 최소 동전의 갯수
dp = [INF] * (K + 1)
# 초기값 설정하는것도 중요하고, 일단 점화식이란게 각 항들간의 관계에 대한 식이란 것도 유념해야겠네
dp[0] = 0
for coin in coins:
    for i in range(coin, K + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])
