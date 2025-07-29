import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())

miro = [[] for _ in range(N)]
# 미로 흰방 = 1 / 검은방 = 0
# 흰방은 지나갈 수 있음
for i in range(N):
    for j in input().rstrip():
        miro[i].append(int(j))

# 검은방에서 흰방으로 바꾸어야 할 최소의 수를 구하라
# 윗줄 맨 왼쪽방(0,0) 시작방
# 아랫줄 맨 오른쪽방(N-1,N-1) 끝방


# for i in range(N):
#     for j in range(N):
#         print(cost[i][j], end=" ")
#     print()





def dijkstra(x, y):
    
    # 이동비용 
    # 흰방 = 0, 검은방 = 1
    cost = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 0:
                cost[i][j] = 1
    
    heap = []
    heapq.heappush(heap, (cost[x][y],x,y))

    # 비용 집계 초기화
    distance = [[1e9] * N for _ in range(N)]               

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while heap:
        dist,node_x,node_y = heapq.heappop(heap)

        if dist > distance[node_x][node_y]:
            continue

        for i in range(4):
            nx = node_x + dx[i]
            ny = node_y + dy[i]

            
            if (0 <= nx < N) and (0 <= ny < N):
                total = dist + cost[nx][ny]

                if total < distance[nx][ny]:
                    distance[nx][ny] = total
                    heapq.heappush(heap,(total,nx,ny))

    return distance[N-1][N-1]

print(dijkstra(0, 0))



