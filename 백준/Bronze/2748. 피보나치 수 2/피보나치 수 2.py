import sys

input = sys.stdin.readline

N = int(input().rstrip())

# 1.문제 목표: N번째 피보나치 수를 구하라
# 2.상태 정의: dp[i]는 무엇인가? i번째 피보나치수의 값
# 3.점화식? 주어짐, dp[n] = dp[n-1] + dp[n-2] (n>=2)
# 4.초기값 dp[0] = 0 , dp[1] = 1
# 5.정답위치는 dp[N]

dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
