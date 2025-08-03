import sys

input = sys.stdin.readline

# 도시의 수
N = int(input().rstrip())
# W[i][j] = 도시i에서 도시 j로 가기 위한 비용
W = [list(map(int, input().rstrip().split())) for _ in range(N)]

dp = {}

def dfs(now, visited):
    # 모든 도시를 방문한 경우
    if visited == (1 << N) - 1:
        # 다시 출발 도시로 갈 수 있는 경우 출발도시까지의 비용 반환
        if W[now][0]:
            return W[now][0]
        else:
            # 갈 수 없는 경우 무한대 반환
            return int(1e9)

    # 이전에 계산된 경우 결과 반환
    if (now, visited) in dp:
        return dp[(now, visited)]  # now 까지 방문한 최소 비용

    min_cost = int(1e9)
    for i in range(1, N):

        # 비용이 0이어서 갈 수 없거나, 이미 방문한 루트면 무시
        if W[now][i] == 0 or visited & (1 << i):
            continue

        cost = dfs(i, visited | (1 << i)) + W[now][i]
        min_cost = min(cost, min_cost)

    dp[((now, visited))] = min_cost  # 현재 경우에서 최소 비용이 드는 루트의 비용 저장
    return min_cost

print(dfs(0,1))