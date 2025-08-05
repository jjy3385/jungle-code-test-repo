import sys

input = sys.stdin.readline

N = int(input().rstrip())

# 그냥 dfs 로 풀릴거 같은데? 아닌듯
# DP 정의해서 푸는 문제 같음
# dp[i] 는 i를 1로 만드는 최소 연산횟수
dp = [0] * (N + 1)
dp[1] = 0

for i in range(2, N + 1):

    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)


print(dp[N])
