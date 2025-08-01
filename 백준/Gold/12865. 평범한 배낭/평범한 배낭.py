import sys

input = sys.stdin.readline

# 물품의 수 N, 버틸 수 있는 무게 K
N, K = map(int, input().rstrip().split())

# 물건의 무게 W, 가치 V
bag = sorted(
    [tuple(map(int, input().rstrip().split())) for _ in range(N)], key=lambda x: x[0]
)

dp = [0] * (K + 1)

for weight, value in bag:
    for i in range(K, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)


print(dp[K])
