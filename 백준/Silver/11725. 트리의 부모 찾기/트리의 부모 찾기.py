import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input().rstrip())
edges = [tuple(map(int, input().rstrip().split())) for _ in range(N - 1)]

tree = defaultdict(list)

# 인접리스트로 표현
for i in range(N - 1):
    a, b = edges[i]
    tree[a].append(b)
    tree[b].append(a)


# dfs 기본형태에 추적하려는 걸 하나 더 파라미터로 추가함
# 여기선 부모
def dfs(node, visited, parent):
    visited[node] = True
    
    # print(node, end=" ")
    for next_node in tree[node]:
        if not visited[next_node]:
            parent[next_node] = node
            dfs(next_node, visited,parent)
            


visited = [False] * (N + 1)
parent = [1] * (N + 1)
dfs(1, visited, parent)

for i in range(2,N+1):
    print(parent[i])
