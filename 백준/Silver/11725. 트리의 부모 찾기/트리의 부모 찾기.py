import sys
from collections import defaultdict,deque

input = sys.stdin.readline

N = int(input().rstrip())
edges = [tuple(map(int, input().rstrip().split())) for _ in range(N - 1)]

tree = defaultdict(list)
# tree = [[] for _ in range(N + 1)]

# 인접리스트로 표현
for i in range(N - 1):
    a, b = edges[i]
    tree[a].append(b)
    tree[b].append(a)

def bfs(node):
    parent = [0] * (N + 1)  # 인덱스 - 현재노드, 값 - 부모노드
    visited = [False] * (N + 1)
    queue = deque([node])
    
    while queue:
        present = queue.popleft()
        for next_node in tree[present]:        
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                parent[next_node] = present


    print("\n".join(str(parent[i]) for i in range(2, N + 1)))


bfs(1)