import sys

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    # 동전의 가지수
    N = int(input().rstrip())
    # 동전종류
    coins = list(map(int, input().rstrip().split()))
    # 만들어야 할 금액
    M = int(input().rstrip())

    dp = [0] * (M + 1)

    dp[0] = 1

    for coin in coins:
        for i in range(1, M + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
        # print(dp)

    print(dp[M])
