
import sys
from collections import deque

input = sys.stdin.readline


# 보드의 크기
N = int(input().rstrip())
# 사과의 개수
K = int(input().rstrip())
# 사과의 위치( 0행0열 시작을 위해 -1 처리)
apples = [
    (int(a) - 1, int(b) - 1) for a, b in (input().rstrip().split() for _ in range(K))
]
# 뱀의 방향변환 횟수
L = int(input().rstrip())
# 뱀의 방향변환 정보 ( D = 오른쪽, L = 왼쪽)
d_changes = [(int(a), b) for a, b in (input().rstrip().split() for _ in range(L))]

# 우하좌상 변량
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 게임시작 준비
snake = deque([(0, 0)])
direction = 0
second = 0
d_info_idx = 0

while True:
    second += 1
    head_x, head_y = snake[0]
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]

    # 벽에 부딛힘 + 자기 몸 좌표으로 가려고함
    if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in snake:
        break

    # 뱀머리 이동
    snake.appendleft((nx, ny))

    # 사과 먹기
    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        # 꼬리 회수
        snake.pop()

    # 회전처리
    if d_info_idx < len(d_changes) and d_changes[d_info_idx][0] == second:
        if d_changes[d_info_idx][1] == "D":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        d_info_idx += 1


print(second)
