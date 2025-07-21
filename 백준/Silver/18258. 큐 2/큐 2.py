class Queue:
    head = 0

    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if self.empty():
            return -1
        else:
            value = self.arr[self.head]
            self.head += 1
            return value

    def size(self):
        return len(self.arr) - self.head

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.arr[self.head]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.arr[-1]


import sys

input = sys.stdin.readline
N = int(input().rstrip())
queue = Queue()

for _ in range(N):
    inputs = input().rstrip().split()
    command = inputs[0]
    element = int(inputs[1]) if len(inputs) > 1 else None

    if command == "push":
        queue.push(element)
    elif command == "pop":
        print(queue.pop())
    elif command == "size":
        print(queue.size())
    elif command == "empty":
        print(queue.empty())
    elif command == "front":
        print(queue.front())
    elif command == "back":
        print(queue.back())
