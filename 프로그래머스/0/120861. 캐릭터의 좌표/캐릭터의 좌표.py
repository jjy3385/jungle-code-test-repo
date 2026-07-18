def solution(keyinput, board):
    x,y = 0,0
    for k in keyinput:
        dx,dy = 0,0
        if k == "left":
            dx = -1
        elif k == "right":
            dx = 1
        elif k == "down":
            dy = -1
        else:
            dy = +1
        
        if abs(x + dx) <= board[0] // 2:
            x += dx
        if abs(y + dy) <= board[1] // 2:
            y += dy

    return [x,y]