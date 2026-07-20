def solution(board):
    answer = 0
    n = len(board)
    dr = [-1,-1,-1,0,0,1,1,1]
    dc = [-1,0,1,-1,1,-1,0,1]
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                        board[nr][nc] = 2
    for r in board:
        for c in r:
            if c == 0:
                answer += 1 

    return answer