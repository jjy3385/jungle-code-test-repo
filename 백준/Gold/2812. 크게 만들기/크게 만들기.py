# K개를 지웠을 때 얻을 수 있는 가장 큰 수 출력
import sys

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
nums = input().strip()

stack = []

# 지울 기회
chance = K
for i in range(N):
    current = int(nums[i])

    while stack and chance > 0:
        if current > stack[-1]:
            stack.pop()
            chance -= 1
        else:
            break

    stack.append(current)
    # print(stack)

if chance > 0:
    stack = stack[:-chance]
print("".join(map(str, stack)))
