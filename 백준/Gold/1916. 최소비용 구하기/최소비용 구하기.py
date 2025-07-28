import sys
import heapq

input = sys.stdin.readline

# 도시의 개수 (노드)
N = int(input().rstrip())
# 버스의 개수 (간선)
M = int(input().rstrip())
# 출발지/도착지/비용
bus = [tuple(map(int, input().rstrip().split())) for _ in range(M)]
# 구하고자 하는 구간 출발 - 도착 도시
goal = tuple(map(int, input().rstrip().split()))
# 최소 비용을 구하라
# 경로가 정해진 경우의 최소 비용 구하기...


# 일단 비용없이 경로 구하기를 bfs 로 만들어보자
graph = [[] for _ in range(N + 1)]


# 거리 배열
INF = int(1e9)
distance = [INF] * (N + 1)

for i in range(M):
    u, v, w = bus[i]
    graph[u].append((v, w))

def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dij(goal[0])

print(distance[goal[1]])