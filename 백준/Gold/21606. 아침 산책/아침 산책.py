import sys
from collections import defaultdict

input = sys.stdin.readline

# 정점의 개수
N = int(input().rstrip())

# 실내 = 1, 실외 = 0
A = input().rstrip()

is_out = [0] * (N + 1)
for i in range(N):
    if A[i] == "1":
        is_out[i + 1] = int(A[i])


graph = defaultdict(list)
# i번째 간선이 u,v 를 각각 연결한다는 의미
for _ in range(N - 1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

    
ans = 0
# path = []
visited = [False] * (N + 1)


# 1. 실외가 없는 경우 - 실내끼리 이어진 경우
for i in range(1, N + 1):
    if is_out[i] == 1:
        # path.append(i)
        for next_place in graph[i]:
            if is_out[next_place] == 1:
                # path.append(next_place)
                ans += 1

def dfs_stack(start):
    result = 0
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        for next_node in graph[node]:
             if not visited[next_node]:
                if is_out[next_node] == 1:
                    result += 1
                else:
                    visited[next_node] = True
                    stack.append(next_node)
    
    return result

# 실외를 기준으로 DFS 해서 실내로 끝나는 경우의 수를 찾기
for i in range(1, N + 1):
    if is_out[i] == 0 and not visited[i]:
        # path.append(i)
        temp = dfs_stack(i)
        # path.pop()
        ans += temp * (temp - 1)

# print(path)
print(ans)
