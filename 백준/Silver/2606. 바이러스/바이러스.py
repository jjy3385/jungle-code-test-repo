import sys
from collections import defaultdict

input = sys.stdin.readline

# 컴퓨터의 수(정점의수)
N = int(input().rstrip())
# 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수(간선의수)
M = int(input().rstrip())

graph = defaultdict(list)

# 그래프 표현
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프 정렬
for i in range(1, N + 1):
    graph[i].sort()


# 스택으로 구현한 dfs
def dfs(start):
    visited = [False] * (N + 1)
    stack = []
    stack.append(start)
    visited[start] = True
    count = 0

    while stack:
        node = stack.pop()
        for i in graph[node]:
            if not visited[i]:
                # 방문처리 시점에 count 올림
                stack.append(i)
                visited[i] = True
                count += 1

    return count


print(dfs(1))
