import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    stack = []
    command = input().rstrip()
    result = "YES"

    for c in command:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                result = "NO"
                break

    if stack:
        result = "NO"

    print(result)
