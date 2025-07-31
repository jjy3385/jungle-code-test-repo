import sys

input = sys.stdin.readline

N = int(input().rstrip())

# 길이가 N인 만들 수 있는 2진 수열의 개수를 15746으로 나눈 나머지 출력

dp = [0] * (N + 2)

dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] % 15746) + (dp[i - 2] % 15746)


print(dp[N] % 15746)
