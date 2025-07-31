import sys
import heapq

input = sys.stdin.readline

# N*N 크기의 시험관 ,K는 바이러스 종류
N, K = map(int, input().rstrip().split())

# 시험관 정보
locations = [list(map(int, input().rstrip().split())) for _ in range(N)]

# S초 지난 후에 (X,Y) 에 존재하는 바이러스의 종류를 출력하라
S, X, Y = map(int, input().rstrip().split())

def bfs():
    global heap
    new_heap = []
    while heap:
        virus, qx, qy = heapq.heappop(heap)
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if ((0 <= nx < N) and (0 <= ny < N)) and locations[nx][ny] == 0:

                locations[nx][ny] = virus
                heapq.heappush(new_heap, (virus, nx, ny))

    heap = new_heap


heap = []

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if locations[i][j] != 0:
            heapq.heappush(
                heap, (locations[i][j], i, j)
            )  # 우선순위 큐에 (바이러스,좌표) 입력

for _ in range(S):
    bfs()

print(locations[X - 1][Y - 1])
