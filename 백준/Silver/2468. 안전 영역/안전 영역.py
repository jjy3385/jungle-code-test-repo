import sys
sys.setrecursionlimit(10**6)

N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]

# 상우하좌 변량
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def find_safety_zone(rain,x,y,visited):

    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if (0 <= nx < N) and (0 <= ny < N) and W[nx][ny] > rain and not visited[nx][ny]:
            visited[nx][ny] = True
            find_safety_zone(rain,nx,ny,visited)


max_counts = []
for rain in range(101):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if W[i][j] > rain and not visited[i][j]:
                count+= 1
                find_safety_zone(rain,i,j,visited)
    max_counts.append(count)

print(max(max_counts))

