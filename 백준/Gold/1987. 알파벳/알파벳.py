import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(R)]

visited = set()

def dfs(r, c, cnt):

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if (0 <= nr < R) and (0 <= nc < C) and board[nr][nc] not in visited:
            visited.add(board[nr][nc])     
            dfs(nr, nc, cnt + 1)
            visited.remove(board[nr][nc])
        else:
            # base case
            res.add(cnt)

res = set() 
visited.add(board[0][0])
dfs(0, 0, 1)
print(max(res))