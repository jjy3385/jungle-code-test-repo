import sys
sys.setrecursionlimit(10**6)

N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]

def dfs(i,j,rain,visited):
    # base case?
    # 1.범위를 벗어난 경우, 왜 여기 안걸리는게 나오는건지 이해가 안가
    # print(f"좌표({i},{j})")
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    # 2. 이미 방문했거나 잠긴경우
    if visited[i][j] or W[i][j] <= rain:
        return 

    visited[i][j] = True
    # 오른쪽 
    dfs(i,j+1,rain,visited)
    # 왼쪽
    dfs(i,j-1,rain,visited)    
    # 위
    dfs(i-1,j,rain,visited)    
    # 아래
    dfs(i+1,j,rain,visited)    


counts = []
# 강수량 올라가는건 그냥 반복호출해도 됨 
for rain in range(101):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if W[i][j] > rain and not visited[i][j]:
                count += 1
                dfs(i,j,rain,visited)
    counts.append(count)
print(max(counts))
