import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

graph = []
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))


# 인접리스트로 바꾸는게 아니고 2차원 배열 그대로 푸는 문제
# x = N -1 , y = M -1 일 때 지나야 하는 최소 칸 수를 구하는 문제
# 잘 이해 안됨
# 어떻게 했다는거지???
# graph 에 +1 하는거랑 최단거리가 구해지는게 이해가 잘 안감
def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        a, b = queue.popleft()

        # 주변 정점 탐색
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < M) and graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                queue.append((nx, ny))

    return graph[N - 1][M - 1]

print(bfs(0, 0))
