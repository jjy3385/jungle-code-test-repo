import sys
from collections import deque

input = sys.stdin.readline
# 정점의 개수 N
# 간선의 개수 M
# 시작정점 V
N, M, V = map(int, input().rstrip().split())

# 인접리스트 초기화
# 정점의 개수 + 1 하는 이유는 인덱스 1부터 사용하기 위해서임
graph = [[] for _ in range(N + 1)]


# 간선이 연결하는 두 정점의 번호
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


# 정점 번호가 작은 순서대로 방문해야 하므로 리스트 정렬
for i in range(1, N + 1):
    graph[i].sort()

# 그래프 확인용 출력
# for i in range(1, N + 1):
#     print(f"{i} => {graph[i]}")


# dfs 는 재귀/스택
def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v, visited)


# bfs 는 큐
def bfs(v):
    visited = [False] * (N + 1)
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
