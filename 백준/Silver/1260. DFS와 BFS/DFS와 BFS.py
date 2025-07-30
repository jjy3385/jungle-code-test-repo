import sys

from collections import defaultdict, deque

input = sys.stdin.readline

# 정점의 개수 N, 간선의 개수M, 시작 정점 V
N, M, V = map(int, input().rstrip().split())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프 정렬
for i in range(1, N + 1):
    graph[i].sort()


def dfs(start, visited):
    visited[start] = True
    print(start, end=" ")
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(next_node,visited)


def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                


visited = [False] * (N + 1)
dfs(V,visited)
print()
bfs(V)
