class stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if self.size() != 0:
            return self.arr.pop()
        else:
            return -1

    def size(self):
        return len(self.arr)

    def empty(self):
        if self.size() != 0:
            return 0
        else:
            return 1

    def top(self):
        if self.size() != 0:
            return self.arr[-1]
        else:
            return -1


import sys

input = sys.stdin.readline

N = int(input().rstrip())

st = stack()
for _ in range(N):
    inputs = input().rstrip().split()
    command = inputs[0]
    element = int(inputs[1]) if len(inputs) > 1 else None

    if command == "push":
        st.push(element)
    elif command == "pop":
        print(st.pop())
    elif command == "size":
        print(st.size())
    elif command == "empty":
        print(st.empty())
    else:
        print(st.top())
