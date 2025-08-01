import sys

input = sys.stdin.readline

# 최대 공부시간 N , 과목 수 K
N, K = map(int, input().rstrip().split())
# (중요도 , 필요한 공부시간)
subjects = sorted(
    [tuple(map(int, input().rstrip().split())) for _ in range(K)], key=lambda x: x[1]
)

# dp 설정
# 얻을 수 있는 최대 중요도
# dp[0] 의 의미 => 0시간동안 얻을 수 있는 중요도 = 0
# dp[N] 의 의미 => 최대 공부시간 N동안 얻을 수 있는 최대 중요도

dp = [0] * (N+1)

for value,weight in subjects:
    for i in range(N,weight -1,-1):
        dp[i] = max(dp[i],dp[i-weight]+ value)
    # print(dp)

print(dp[N])