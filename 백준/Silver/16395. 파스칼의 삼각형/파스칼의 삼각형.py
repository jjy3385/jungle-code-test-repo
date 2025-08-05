import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
# N번째 행에 K번째 수를 출력

# 바로 점화식이 나오는 형태인가?
# dp[n][k] = dp[n-1][k-1] + dp[n-1][k]
# 다 필요한것도 아니긴해서.. 
# dp[N][K] 를 구한다면...

dp = []
for i in range(1,N+1):
    dp.append([0 for _ in range(i)])

dp[0][0] = 1
for i in range(N):
    for j in range(i+1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[N-1][K-1])