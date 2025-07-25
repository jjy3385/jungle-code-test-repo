import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# 도시의 개수 N
# 도로의 개수 M
# 거리 정보 K
# 출발 도시의 번호 X
N, M, K, X = map(int, input().rstrip().split())

# 그래프로 표현
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)


def bfs(start):
    visited = [-1] * (N + 1)
    visited[start] = 0
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()
        for next_v in graph[node]:
            if visited[next_v] == -1:
                visited[next_v] = dist + 1
                queue.append((next_v, visited[next_v]))

    return visited


# 최단거리가 K 인 도시 리스트 구하기
visited = bfs(X)

res = []
for i in range(N + 1):
    if visited[i] == K:
        res.append(i)


if res:
    print("\n".join(map(str, res)))
else:
    print(-1)
