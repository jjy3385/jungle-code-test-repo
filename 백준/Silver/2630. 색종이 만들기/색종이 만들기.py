
import sys

input = sys.stdin.readline
N = int(input().rstrip())
S = [list(map(int, input().rstrip().split())) for _ in range(N)]


w_count = 0
b_count = 0


# n 한변의 길이
# x,y 시작좌표
def recursive(n, x, y):
    # print(f"n = {n}, x = {x}, y = {y}")
    global w_count, b_count

    if n == 0:
        return

    start = S[x][y]
    count = True
    for i in range(n):
        for j in range(n):
            if S[x + i][y + j] != start:
                count = False

    # print(f"start = {start}, count = {count}")

    if count:
        if start == 0:
            w_count += 1
            return
        else:
            b_count += 1
            return
    else:
        recursive(n // 2, x, y)
        recursive(n // 2, x + n // 2, y)
        recursive(n // 2, x, y + n // 2)
        recursive(n // 2, x + n // 2, y + n // 2)


recursive(N, 0, 0)
print(w_count)
print(b_count)
