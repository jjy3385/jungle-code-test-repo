import sys

sys.setrecursionlimit(10**6)
# 입력개수를 안알려줌
preorder = list(map(int, sys.stdin.read().split()))

result = []


def dfs(start, end):
    if start > end:
        return

    root = preorder[start]

    mid = start + 1
    while mid <= end and preorder[mid] < root:
        mid += 1

    dfs(start + 1, mid - 1)
    dfs(mid, end)
    result.append(root)


dfs(0, len(preorder) - 1)

print("\n".join(map(str, result)))
