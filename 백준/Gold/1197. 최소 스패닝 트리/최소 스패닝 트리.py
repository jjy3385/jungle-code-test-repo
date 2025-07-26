import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
V, E = map(int, input().rstrip().split())

edges = []
for _ in range(E):
    A, B, C = map(int, input().rstrip().split())
    edges.append((A, B, C))

# 프림 알고리즘

# 그래프 선언
graph = defaultdict(list)

# 간선 정보
# edges = [(1, 2, 3), (1, 3, 2), (2, 3, 1), (2, 4, 4), (3, 4, 5), (4, 5, 7), (3, 5, 6)]

# 무방향 그래프 구성
for u, v, w in edges:
    graph[u].append((w, v))  # (가중치,목적지)
    graph[v].append((w, u))  # 양방향 추가


# Prim 알고리즘 시작
def prim(start):
    visited = set()  # 방문한 정점
    min_heap = []  # 우선순위 큐
    total_cost = 0  # 최소 비용 합계

    # 초기 노드에서 갈 수 있는 간선들 큐에 삽입
    visited.add(start)
    for weight, neighbor in graph[start]:
        heapq.heappush(min_heap, (weight, neighbor))

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node in visited:
            continue  # 이미 연결된 정점은 무시

        visited.add(node)
        total_cost += weight

        for next_weight, next_node in graph[node]:
            if next_node not in visited:
                heapq.heappush(min_heap, (next_weight, next_node))

    return total_cost

print(prim(1))