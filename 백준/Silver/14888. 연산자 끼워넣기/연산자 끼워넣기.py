import sys

input = sys.stdin.readline
# 수의 개수
N = int(input().rstrip())
# 정점의 값
A = list(map(int, input().rstrip().split()))
# 덧셈의수/뺼셈의수/곱셈의수/나눗셈의수
# 합이 N - 1
B = list(map(int, input().rstrip().split()))
# 구해야하는 것은 이걸 조합해서 얻을 수 있는 최대값/최소값
# 각 숫자가 노드임
# N의 최대값이 11
# 즉 연산자가 10개인 경우가 최대 갯수
# 연산자가 4종류이니까 2 ** 20 까지 조합이 발생할 수 있는건가??


path = []
max_v = int(-1e9)
min_v = int(1e9)


def dfs(depth, total, plus, minus, multi, divide):
    global max_v, min_v
    # base case
    # dfs 호출 한번이 숫자 하나를 선택했다는 걸 의미
    # 따라서 depth == N은 N개의 숫자를 모두 선택했다는 뜻(경로를 끝까지 탐색했다)
    if depth == N - 1:

        max_v = max(total, max_v)
        min_v = min(total, min_v)
        return

    nums = A[depth + 1]
    # 더하기
    if plus:
        new_total = total + nums
        dfs(depth + 1, new_total, plus - 1, minus, multi, divide)
    # 빼기
    if minus:
        new_total = total - nums
        dfs(depth + 1, new_total, plus, minus - 1, multi, divide)
    # 곱하기
    if multi:
        new_total = total * nums
        dfs(depth + 1, new_total, plus, minus, multi - 1, divide)
    # 나누기
    if divide:
        if total < 0:
            total = -total
            new_total = (total // nums) * -1
        else:
            new_total = total // nums
        dfs(depth + 1, new_total, plus, minus, multi, divide - 1)


dfs(0, A[0], B[0], B[1], B[2], B[3])
print(max_v)
print(min_v)
