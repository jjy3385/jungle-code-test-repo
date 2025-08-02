import sys

input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))


# LDS 라고 부르나?
# LCS 랑 똑같다고 하면 dp[i] = A[i] 를 마지막 원소로 갖는 가장 긴 감소하는 부분수열의 길이

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)


print(max(dp))