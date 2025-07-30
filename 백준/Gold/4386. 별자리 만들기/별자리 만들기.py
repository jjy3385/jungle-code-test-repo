import sys
from itertools import permutations
import math

input = sys.stdin.readline
N = int(input().rstrip())

stars = {}
for i in range(N):
    x, y = map(float, input().rstrip().split())
    stars[i + 1] = (x, y)

# 별 2개를 고르는 순열
# 별 간의 거리를 담은 간선 생성
edges = []
for a, b in permutations(stars, 2):
    x0, y0 = stars[a]
    x1, y1 = stars[b]
    dist = int(math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2) * 100) / 100
    edges.append((a, b, dist))

# 거리 기준 오름차순 정렬
edges.sort(key=lambda x: x[2])


# 크루스칼 알고리즘 시작

# 1.parent 선언(정점 + 1 개)
parent = [i for i in range(N + 1)]

# 2. union find 함수 선언
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 3. 비용 집계
# 항상 간선 기준으로, 크루스칼은 비용인 낮은 간선부터 추가하는 알고리즘임
cost = 0
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        cost += c

print(cost)