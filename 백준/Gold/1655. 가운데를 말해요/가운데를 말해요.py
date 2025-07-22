

class MyMaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        index = len(self.heap) - 1

        # 새로 입력된 수가 부모보다 크면 SWAP
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                # 스왑 안되면 명시적으로 탈출해주는게 좋다
                break

    def pop(self):

        # 루트랑 마지막 원소 스왑
        index = len(self.heap) - 1

        if index < 0:
            return 0

        self.heap[0], self.heap[index] = (
            self.heap[index],
            self.heap[0],
        )

        pop_value = self.heap.pop()

        # 루트 제자리 찾기
        root = 0
        while True:

            left_c = 2 * root + 1
            right_c = 2 * root + 2
            result = root

            if left_c < len(self.heap) and self.heap[left_c] > self.heap[result]:
                result = left_c
            if right_c < len(self.heap) and self.heap[right_c] > self.heap[result]:
                result = right_c

            # 자식이 없거나 현재 최대힙이 유지되서 바꿀 필요가 없으면
            if result == root:
                break

            self.heap[root], self.heap[result] = (self.heap[result], self.heap[root])
            root = result

        return pop_value


class MyMinHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        index = len(self.heap) - 1

        # 새로 입력된 수가 부모보다 크면 SWAP
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                # 스왑 안되면 명시적으로 탈출해주는게 좋다
                break

    def pop(self):

        # 루트랑 마지막 원소 스왑
        index = len(self.heap) - 1

        if index < 0:
            return 0

        self.heap[0], self.heap[index] = (
            self.heap[index],
            self.heap[0],
        )

        pop_value = self.heap.pop()

        # 루트 제자리 찾기
        root = 0
        while True:

            left_c = 2 * root + 1
            right_c = 2 * root + 2
            result = root

            if left_c < len(self.heap) and self.heap[left_c] < self.heap[result]:
                result = left_c
            if right_c < len(self.heap) and self.heap[right_c] < self.heap[result]:
                result = right_c

            # 자식이 없거나 현재 최대힙이 유지되서 바꿀 필요가 없으면
            if result == root:
                break

            self.heap[root], self.heap[result] = (self.heap[result], self.heap[root])
            root = result

        return pop_value


import sys

input = sys.stdin.readline
N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]

min_heap = MyMinHeap()
max_heap = MyMaxHeap()

for n in nums:
    max_heap.push(n)

    if min_heap.heap and max_heap.heap[0] > min_heap.heap[0]:
        max_val = max_heap.pop()
        min_val = min_heap.pop()
        max_heap.push(min_val)
        min_heap.push(max_val)

    while len(max_heap.heap) - 1 > len(min_heap.heap):
    # while len(max_heap.heap) > len(min_heap.heap) + 1:
        min_heap.push(max_heap.pop())

    print(max_heap.heap[0])
    # print(f"max:{max_heap.heap}")
    # print(f"min:{min_heap.heap}")

