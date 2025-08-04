import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
stones = [int(input().rstrip()) for _ in range(M)]


def bfs(now, jump):
    # visited = [[False] * (N + 1) for _ in range(N + 1)]  # visited[현재돌][점프] 
    # 이거 메모리 초과남
    visited = set()
    visited.add((now, jump))
    queue = deque([(now, jump, 0)])  # (현재돌,점프,점프횟수)

    while queue:

        prev_stone, prev_jump, prev_cnt = queue.popleft()
        # print(prev_stone, prev_jump, prev_cnt)

        if prev_stone == N:
            return prev_cnt

        for d in [-1, 0, 1]:
            next_jump = prev_jump + d
            next_stone = prev_stone + next_jump

            if (
                next_jump > 0
                and next_stone <= N
                and next_stone not in stones
                and (next_stone,next_jump) not in visited
            ):
                queue.append((next_stone, next_jump, prev_cnt + 1))
                visited.add((next_stone,next_jump))

    return -1


print(bfs(1, 0))
