import sys

input = sys.stdin.readline
# 도시의 개수 N , 버스의 개수 M
N = int(input().rstrip())
M = int(input().rstrip())


# 모든 최단거리를 저장할 이차원배열
INF = 1e9
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            dist[i][j] = 0


# 시작도시/도착도시/비용
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    dist[a][b] = min(c, dist[a][b])


# 플로이드-워셜은 모든 최단 경로를 구하는 알고리즘
# 1. 모든 최단거리를 저장할 이차원배열 선언
# 2. 이차원배열에 비용 입력, 서로 인접한 경우에만 비용이 들어가고 그 외의 경우는 INF
# 3. k번 노드를 새로운 중간 노드로 설정

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
