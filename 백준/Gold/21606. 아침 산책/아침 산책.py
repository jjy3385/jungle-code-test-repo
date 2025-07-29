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

# 서로 다른 산책 경로의 수를 구하라
# 실외에서 시작되고 다시 실외를 찾으면 +1 한다고 생각하면 됨
visited = [False] * (N + 1)


# 이 함수가 하는 일이 뭐지?
# 주변 탐색하는거임
# 무조건 실내임
# 실외로 가면 + 1
def dfs(start):
    res = 0 
    for next_node in graph[start]:
        if is_out[next_node] == 0:
            if not visited[next_node]:
                visited[next_node] = True
                res += dfs(next_node)
        else:
            res += 1
    return res


answer = 0
for i in range(1, N + 1):
    if is_out[i] == 0:
        if not visited[i]:
            visited[i] = True
            result = dfs(i)
            answer = result * (result - 1)
    else:
        for next_node in graph[i]:
            if is_out[next_node] == 1:
                answer += 1


print(answer)
