import sys

input = sys.stdin.readline

check_str = input().rstrip()
ex_str = list(input().rstrip())

stack = []
length = len(ex_str)

for i in check_str:
    stack.append(i)

    # 슬라이싱 아직 헷갈림/ 활용 자체도 못하는듯
    if stack[-length:] == ex_str:
        for _ in range(length):
            stack.pop()


if stack:
    print("".join(stack))
else:
    print("FRULA")
