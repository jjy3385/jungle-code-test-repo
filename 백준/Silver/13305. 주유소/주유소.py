import sys

input = sys.stdin.readline
# 도시의 개수
N = int(input().rstrip())
# 인접한 두 도시를 연결하는 도로의 길이
roads = list(map(int, input().rstrip().split()))
# 주유소의 리터당 가격
prices = list(map(int, input().rstrip().split()))

cost = 0
min_price = prices[0]
for i in range(N):

    if i == N - 1:
        break
    # 최소 기름값 갱신
    if min_price > prices[i]:
        min_price = prices[i]

    cost += min_price * roads[i]

print(cost)
