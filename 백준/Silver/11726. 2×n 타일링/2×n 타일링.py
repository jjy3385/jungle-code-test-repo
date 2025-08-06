import sys

input = sys.stdin.readline
N = int(input().rstrip())

dp = [0] * (N + 1)


if N <= 2:
    print(N)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    print(dp[N])
