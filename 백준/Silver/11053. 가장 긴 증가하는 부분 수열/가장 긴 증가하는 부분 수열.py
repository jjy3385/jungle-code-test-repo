import bisect

N = int(input())
A = list(map(int, input().split()))

dp = []

for x in A:
    idx = bisect.bisect_left(dp, x)
    if idx == len(dp):
        dp.append(x)
    else:
        dp[idx] = x

print(len(dp))