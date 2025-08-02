import sys

input = sys.stdin.readline
# 동전의 종류 N, 가치의 합 K
N, K = map(int, input().rstrip().split())
# 동전의 종류
coins = [int(input().rstrip()) for _ in range(N)]

count = 0
remain = K 
for coin in sorted(coins, reverse=True):
    if remain >= coin:
        count += remain // coin
        remain = remain % coin

print(count)

