import sys

input = sys.stdin.readline
# 동전의 종류 N, 가치의 합 K
N, K = map(int, input().rstrip().split())
# 동전의 종류
coins = [int(input().rstrip()) for _ in range(N)]

# K원을 만들기 위해 필요한 동전의 개수 최솟값
remain = K

count = 0
while remain > 0:

    i = 0
    while (0 <= i < N) and coins[i] <= remain:
        i += 1
    i -= 1
    
    # print(remain, coins[i])
    remain -= coins[i]
    count += 1


# print(remain)
print(count)
