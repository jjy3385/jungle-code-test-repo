N = int(input())
A = list(map(int,input().split()))
visited = [False] * N
path = []
max_values = []
def dfs(n):
    global max_value
    # base case
    if n == N:
        # print(path)
        max_values.append(sum([abs(path[i] - path[i+1]) for i in range(N-1)]))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            path.append(A[i])
            dfs(n+1)
            visited[i] = False
            path.pop()

dfs(0)

print(max(max_values))
