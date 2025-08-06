import sys

input = sys.stdin.readline

# 계단의 개수
N = int(input().rstrip())
# 각 계단에 쓰여있는 점수
scores = [0] + [int(input().rstrip()) for _ in range(N)]

dp = [0] * (N + 1)

if N >= 1:
    dp[1] = scores[1]
if N >= 2:
    dp[2] = scores[1] + scores[2]
if N >= 3:
    # 3번째 계단 밟았으니까 scores[3] 은 항상 포함되어야 함
    # 그리고 이제 1번 밟았거나 2번 밟았거나 둘 중 큰 게 dp[3]
    dp[3] = max(scores[1] + scores[3], scores[2] + scores[3])

for i in range(4, N + 1):
    dp[i] = max(dp[i - 3] + scores[i - 1], dp[i - 2]) + scores[i]
    
print(dp[N])
