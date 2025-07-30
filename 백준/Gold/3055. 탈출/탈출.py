import sys
from collections import deque

input = sys.stdin.readline
# 지도의 크기 R행 C열
R, C = map(int, input().rstrip().split())

# 2차원 지도
maps = [["."] * C for _ in range(R)]

for i in range(R):
    temp = input().rstrip()
    for j in range(C):
        if temp[j] != ".":
            maps[i][j] = temp[j]


# 고슴도치 이동 큐
queue = deque()

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 고슴도치는 visited 가 필요
visited = [[False] * C for _ in range(R)]

# 1.맵에서 물 찾아서 큐에 다 넣기
for i in range(R):
    for j in range(C):
        # 물
        if maps[i][j] == "*":
            queue.append((0, maps[i][j], i, j))

# 2.맵에서 고슴도치 위치 찾아서 넣기
for i in range(R):
    for j in range(C):
        # 고슴도치 시작위치
        if maps[i][j] == "S":
            visited[i][j] = True
            queue.append((0, maps[i][j], i, j))  # 분(시간),S=>고슴도치,* => 물,좌표


# 2.큐에서 빼면서 물->확장, 고슴도치 이동
# 최소힙 써야하나? 항상 물이 고슴도치보다 먼저 확장하는게 맞을거 같은데?
# 근데 또 그렇지가 않음, 그렇게 하면 서로 턴 개념이 깨짐
# 위에서처럼 반복문을 쪼개면 턴 깨지지 않음 -> GPT 힌트였다

res = 0
while queue:
    minutes, kind, x, y = queue.popleft()

    # 1. 물부터 확장
    if kind == "*":
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < R) and (0 <= ny < C) and maps[nx][ny] not in ["X", "D", "*"]:
                maps[nx][ny] = "*"
                queue.append((minutes + 1, kind, nx, ny))

    # 2. 고슴도치 이동
    if kind == "S":
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < R) and (0 <= ny < C):

                # 도착 시
                if maps[nx][ny] == "D":
                    print(minutes + 1)
                    sys.exit(0)

                # 다음 칸으로 이동 시
                if maps[nx][ny] == "." and not visited[nx][ny]:
                    visited[nx][ny] = True
                    maps[nx][ny] = "S"
                    queue.append((minutes + 1, kind, nx, ny))
    


print("KAKTUS")
