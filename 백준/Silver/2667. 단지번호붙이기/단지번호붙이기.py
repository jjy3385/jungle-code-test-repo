import sys
from collections import deque

input = sys.stdin.readline
# 정사각형의 크기 N ,
N = int(input().rstrip())

# 단지 이차월 배열
danji = [[0] * N for _ in range(N)]

for i in range(N):
    inputs = input().rstrip()
    for j in range(N):
        danji[i][j] = int(inputs[j])



visited = [[False] * N for _ in range(N)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = 1
    while queue:
        qx, qy = queue.popleft()

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if ((0 <= nx < N) and (0 <= ny < N)) and danji[nx][ny] == 1:
                if not visited[nx][ny]:
                    count += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return count
                    
res = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and danji[i][j] == 1:
            res.append(bfs(i,j))

res.sort()
print(len(res))
print("\n".join(map(str,res)))