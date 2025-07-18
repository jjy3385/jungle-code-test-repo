import sys

input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().rstrip().split())))

left = 0  # 알칼리
right = N - 1  # 산성

min_diff = float('inf')

best_left = 0
best_right = 0

while left < right:

    check_sum = A[left] + A[right]

    if abs(check_sum) < min_diff:
        min_diff = abs(check_sum)
        best_left = left
        best_right = right

    if check_sum < 0:
        left += 1
    elif check_sum > 0:
        right -= 1
    elif check_sum == 0:
        break

print(A[best_left],A[best_right])
