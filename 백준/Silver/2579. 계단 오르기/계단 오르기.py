import sys

input = sys.stdin.readline

# 계단의 개수
N = int(input().rstrip())
# 각 계단에 쓰여있는 점수
scores = [int(input().rstrip()) for _ in range(N)]

dp = [0] * (N + 1)

# 이런게 뭐 점수가 있거나 무게가 있거나 이런 애들은 + scores[i] 이런게 붙음
# 대충 dp[i] = dp[i] + scores[i] 이런 느낌으로
# 이 문제에서 일단 dp[i] 는 i번째 계단을 밟았을 때 얻는 총점이니까 dp[i-1] 이나 dp[i-2] 이 둘의 총점 max + 이번 scores[i] 합친게 되겠네

if N == 1:
    print(scores[0])
elif N == 2:
    print(scores[0] + scores[1])
elif N == 3:
    print(max(scores[0] + scores[2], scores[1] + scores[2]))
else:
    dp[1] = scores[0]
    dp[2] = scores[0] + scores[1]
    dp[3] = max(scores[0] + scores[2], scores[1] + scores[2])

    # print(dp[1], dp[2], dp[3])
    for i in range(4, N + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + scores[i - 2]) + scores[i - 1]

    print(dp[N])