import sys

input = sys.stdin.readline

# 도시의 수
N = int(input().rstrip())
# W[i][j] = 도시i에서 도시 j로 가기 위한 비용
W = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 우리가 구하는 것은 외판원이 순회에 필요한 최소비용이다

# 유명한 외판원 순회문제
# for i in range(N):
#     for j in range(N):
#         print(W[i][j], end=" ")
#     print()


def dfs(depth, current, start, cost):
    if depth == N - 1:

        if W[current][start] != 0:
            total_cost = cost + W[current][start]
            # print(f"path = {path}, cost = {total_cost}")
            costs.append(total_cost)
        return

    for i in range(N):
        if not visited[i] and W[current][i] != 0:
            visited[i] = True
            path.append(i)
            new_cost = cost + W[current][i]
            dfs(depth + 1, i, start, new_cost)
            visited[i] = False
            path.pop()


visited = [False] * N
visited[0] = True
path = []
costs = []
dfs(0, 0, 0, 0)
print(min(costs))
