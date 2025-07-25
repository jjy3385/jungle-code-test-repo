import sys
from collections import defaultdict, deque

input = sys.stdin.readline
# N명의 학생, M번 키를 비교함
N, M = map(int, input().rstrip().split())

# 진입차수
indegree = [0] * (N + 1)
graph = defaultdict(list)

for _ in range(M):
    # 키를 비교한 두 학생 A,B 키는 A < B 라는 뜻
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)
    indegree[B] += 1


def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        result.append(node)

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()