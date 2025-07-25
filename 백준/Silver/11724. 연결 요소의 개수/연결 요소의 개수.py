import sys
from collections import defaultdict, deque

input = sys.stdin.readline
# 정점의 개수 N , 간선의 개수 M
# 연결 요소가 뭐지??
N, M = map(int, input().rstrip().split())

graph = defaultdict(list)

# 1. 그래프의 표현
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


# 2. 그래프 정렬
for i in range(1, N + 1):
    graph[i].sort()

# 3.그래프 출력해보기
# for i in range(1, N + 1):
#     print(f"{i} => {graph[i]}")


# 4.그래프 순회, dfs,bfs 아무거나 써도 상관없음
# dfs
def dfs(v, visited):
    visited[v] = True
    # print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)


def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        # 이거 거꾸로 넣어서 앞으로 빼는 모습을 상상해줘야됨
        v = queue.popleft()
        # print(v, end=" ")
        for next_v in graph[v]:
            if not visited[next_v]:
                queue.append(next_v)
                visited[next_v] = True


# 5.근데 이 문제느 연결요소를 묻는 문제임, 그러니까 전체 visited 가 다 True 가 될 때까지 시작이 몇번 바뀌면 되냐는건데

visited = [False] * (N + 1)
count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, visited)
        count += 1

print(count)
