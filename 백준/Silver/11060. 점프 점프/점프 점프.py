import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))


def bfs(start):

    queue = deque([(start, A[start], 0)])
    visited = set((start, A[start]))  # 현재 칸, 점프 한계
    while queue:
        now, jump, cnt = queue.popleft()

        # print(now, jump, cnt)
        if now == N - 1:
            return cnt

        for j in range(jump + 1):
            nxt = now + j
            if nxt < N and (nxt, j) not in visited:
                visited.add((nxt, j))
                queue.append((nxt, A[nxt], cnt + 1))
    return -1

print(bfs(0))
