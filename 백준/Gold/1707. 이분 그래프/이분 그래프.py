import sys
from collections import defaultdict, deque

input = sys.stdin.readline

K = int(input().rstrip())


def bfs(graph, start,visited):

    queue = deque([start])
    
    # 시작정점을 1로 표시
    visited[start] = 1

    # 이분 그래프 여부 
    res = True

    while queue:
        node = queue.popleft()
 
        for next_node in graph[node]:
            if visited[next_node] == 0:
                if visited[node] == 1:
                    visited[next_node] = -1
                else:
                     visited[next_node] = 1
                queue.append(next_node)
            else:
                if visited[next_node] == visited[node]:
                    return False
                          
    return res
                    
                    
for _ in range(K):
    # 정점의 개수 V, 간선의 개수 E
    V, E = map(int, input().rstrip().split())
    UV = [tuple(map(int, input().rstrip().split())) for _ in range(E)]

    # 그래프 표현
    graph = defaultdict(list)

    for i in range(E):
        u, v = UV[i]
        graph[u].append(v)
        graph[v].append(u)

    res = True
    visited = [0] * (V + 1)

    # 시작점을 돌아가보며 확인 필요
    for i in range(1, V + 1):
        if visited[i] == 0:
            if not bfs(graph, i,visited):
                res = False
                break
        
    if res:
        print("YES")
    else:
        print("NO")