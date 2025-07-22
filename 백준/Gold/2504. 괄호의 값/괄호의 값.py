# 괄호 안에 있으면 곱해짐
# 완성된 괄호끼리는 더해짐
# 그니까 아직 열려있을 땐 곱할 준비를 해야되고
# 이거 그 스택을 이용한 후위연산같은데

import sys

input = sys.stdin.readline
inputs = input().rstrip()
stack = []

for c in inputs:

    if c in ["(", "["]:
        stack.append(c)

    else:
        temp = 0
        while stack:
            top = stack.pop()

            if isinstance(top, int):
                temp += top
            elif (c == ")") and top == "(" or (c == "]") and top == "[":
                if temp == 0:
                    stack.append(2 if c == ")" else 3)
                else:
                    stack.append(temp * (2 if c == ")" else 3))
                break
            else:
                print(0)
                exit(0)
        else:
            print(0)
            exit(0)

result = 0
for item in stack:
    if isinstance(item, int):
        result += item
    else:
        print(0)
        exit(0)

print(result)
