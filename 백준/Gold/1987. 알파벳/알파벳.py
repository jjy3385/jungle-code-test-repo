import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, cnt, visited):
    global max_cnt
    # 상하좌우
    max_cnt = max(max_cnt, cnt)

    # print(bin(visited))

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if (0 <= nr < R) and (0 <= nc < C):

            bit = ord(board[nr][nc]) - ord("A")

            if visited & (1 << bit) == 0:
                visited |= 1 << bit
                dfs(nr, nc, cnt + 1, visited)
                visited &= ~(1 << bit)


max_cnt = 0
start_bit = ord(board[0][0]) - ord("A")
dfs(0, 0, 1, (1 << start_bit))
print(max_cnt)
