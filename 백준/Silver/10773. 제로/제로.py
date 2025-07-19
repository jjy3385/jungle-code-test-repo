import sys

input = sys.stdin.readline
K = int(input().rstrip())

stack = []
for _ in range(K):
    s = int(input().rstrip())
    if s == 0:
        stack.pop()
    else:
        stack.append(s)

print(sum(stack))