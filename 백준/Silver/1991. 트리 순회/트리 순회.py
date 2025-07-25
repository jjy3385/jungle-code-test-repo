import sys

# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N = int(input().rstrip())

tree = {}

for _ in range(N):
    root, left, right = input().rstrip().split()
    tree[root] = (left, right)


def preorder(node):

    # base case
    if node == ".":
        return

    left, right = tree[node]
    print(node, end="")

    if left != ".":
        preorder(left)

    if right != ".":
        preorder(right)


def inorder(node):

    # base case
    if node == ".":
        return

    left, right = tree[node]

    if left != ".":
        inorder(left)

    print(node, end="")

    if right != ".":
        inorder(right)


def postorder(node):

    # base case
    if node == ".":
        return

    left, right = tree[node]

    if left != ".":
        postorder(left)

    if right != ".":
        postorder(right)

    print(node, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
print()
