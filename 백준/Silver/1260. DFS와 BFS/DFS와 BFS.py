
import sys
from collections import defaultdict, deque

# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
# 정점의 개수 N
# 간선의 개수 M
# 시작정점 V
N, M, V = map(int, input().rstrip().split())

# 1.그래프의 표현 - 인접리스트
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


# 2.그래프 정렬 -  필요함
# 다음 방문 정점이 결정되기 때문에 결과가 달라짐
for i in range(1, N + 1):
    graph[i].sort()


# dfs - 재귀
def dfs(v, visited):
    # base case
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)


# bfs - 큐
def bfs(v):
    visited = [False] * (N + 1)

    # 시작정점 방문처리
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for next_v in graph[v]:
            if not visited[next_v]:
                queue.append(next_v)
                visited[next_v] = True


visited = [False] * (N + 1)
dfs(V, visited)
print()
bfs(V)