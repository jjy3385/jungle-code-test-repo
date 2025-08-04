import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
stones = [int(input().rstrip()) for _ in range(M)]

dp = {}
dx = [-1, 0, 1]
INF = int(1e9)


def dfs_dp(now, x):

    #print(dp)
    # base case
    if now == N:
        return 0

    # 이미 지나갔던 경로인 경우
    if (now, x) in dp:
        return dp[(now, x)]

    min_junp = INF
    for i in range(3):

        nx = x + dx[i]
        nxt = now + nx

        if nx > 0 and nxt <= N and nxt not in stones:
            jump = dfs_dp(nxt, nx)
            if jump != INF:
                min_junp = min(min_junp, jump + 1)

    dp[(now, x)] = min_junp
    return min_junp


ans = dfs_dp(1, 0)
print(ans if ans != INF else -1)
