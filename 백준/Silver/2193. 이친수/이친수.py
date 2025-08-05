import sys

input = sys.stdin.readline

N = int(input().rstrip())

# dp[i] i자리 이친수의 개수
# 이친수나 01타일은 똑같은 문제임
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
