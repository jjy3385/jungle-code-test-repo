import sys
from collections import deque

input = sys.stdin.readline

# M - 가로/N - 세로/H - 높이
M, N, H = map(int, input().rstrip().split())


# 3차원 배열 만들기
tomatos = [[[0] * M for _ in range(N)] for h in range(H)]

for i in range(H):
    for j in range(N):
        inputs = list(map(int, input().rstrip().split()))
        for k in range(M):
            tomatos[i][j][k] = inputs[k]
            
def bfs():
    queue = deque()

    # 1. 3차원 돌면서 익은 토마토 큐에 삽입
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatos[i][j][k] == 1:
                    queue.append((0, k, j, i))  # (날짜,좌표 - 가로,세로,높이)

    # 상하좌우앞뒤
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    max_day = 0
    # 익은 토마토의 인접 토마토 탐색
    while queue:
        days, x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if ((0 <= nx < M) and (0 <= ny < N) and (0 <= nz < H)) and tomatos[nz][ny][
                nx
            ] == 0:
                tomatos[nz][ny][nx] = 1
                queue.append((days + 1, nx, ny, nz))

        max_day = max(max_day, days)

    res = max_day
    # 토마토 전부 익었는지 확인
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatos[i][j][k] == 0:
                    res = -1
                    break

    return res

print(bfs())
