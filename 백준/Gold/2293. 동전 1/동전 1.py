import sys

input = sys.stdin.readline

# N가지 종류의 동전으로 K원 만들기
N, K = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(N)]

# dp[k] 는 N가지 종류의 동전을 사용하여 k원이 되는 경우의 수
dp = [0] * (K + 1)
# 동전 몇개를 쓰던 0원이 되는 경우는 항상 1가지
dp[0] = 1
for coin in coins:
    for i in range(1,K+1):
        if i >= coin:
            dp[i] += dp[i-coin]

print(dp[K])
