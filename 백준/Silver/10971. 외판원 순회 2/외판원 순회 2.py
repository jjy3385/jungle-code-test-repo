N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]

visited = [False] * N
path = []
depth = 0
min_costs = []

def dfs_last(depth,cost,current,start):
    # base case
    if depth == N:
        if W[current][start] != 0:
            min_costs.append(cost + W[current][start])        
        return

    for i in range(N):
        if not visited[i] and W[current][i] != 0:
            visited[i] = True
            path.append(i)

            new_cost = cost + W[current][i]
        
            # 기준도시도 바뀐다
            dfs_last(depth + 1,new_cost,i,start)
            
            path.pop()
            visited[i] = False

visited[0] = True
path.append(0)
dfs_last(1,0,0,0)

print(min(min_costs))


