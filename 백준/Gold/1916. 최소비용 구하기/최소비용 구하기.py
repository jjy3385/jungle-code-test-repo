import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

# 도시의 수
N = int(input().rstrip())
# 버스의 수
M = int(input().rstrip())

edges = defaultdict(list)
# 연결정보 출발/도착/비용
for i in range(M):
    s, e, c = map(int, input().rstrip().split())
    edges[s].append((e, c))

# 출발지,도착지
start, end = map(int, input().rstrip().split())

distance = [int(1e9)] * (N + 1)


def dijkstra(start,end):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if node == end:
            print(distance[node])
            sys.exit(0)

        if dist > distance[node]:
            continue

        for next_node, next_dist in edges[node]:
            new_dist = next_dist + dist
            if distance[next_node] > new_dist:
                distance[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))


dijkstra(start,end)
# print(distance[end])
