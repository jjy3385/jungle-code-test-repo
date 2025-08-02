import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))


dp = [1] * N
# dp의 정의는 A[i]를 마지막으로 하는 부분 수열 중 가장 긴 증가하는 부분수열의 길이
prev = [-1] * N 
# 이전 원소의 인덱스 저장


for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j
    # print(dp)
    # print(prev)


max_len = max(dp)
last_idx = dp.index(max_len)

res = []
while last_idx != -1:
    res.append(A[last_idx])
    last_idx = prev[last_idx]

res.reverse()

print(max_len)
print(" ".join(map(str,res)))

