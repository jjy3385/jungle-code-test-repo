import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

# 정점의 개수 , 간선의 개수
V, E = map(int, input().rstrip().split())
# 시작정점의 번호
K = int(input().rstrip())
edges = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    edges[u].append((v, w))

INF = 1e9
distance = [INF] * (V + 1)


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        # 노드의 비용이 더 큰 경우는 탐색 필요없음
        if dist > distance[node]:
            continue

        for next_node, next_dist in edges[node]:
            temp_dist = dist + next_dist
            if temp_dist < distance[next_node]:
                distance[next_node] = temp_dist
                heapq.heappush(heap, (temp_dist, next_node))


dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
