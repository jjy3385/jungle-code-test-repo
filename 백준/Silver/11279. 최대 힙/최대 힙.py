class MyMaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        last_index = len(self.heap) - 1

        if last_index != 0:

            # 새로 입력된 수가 부모보다 크면 SWAP
            while last_index > 0:
                parent_index = (last_index - 1) // 2
                if self.heap[last_index] > self.heap[parent_index]:
                    self.heap[last_index], self.heap[parent_index] = (
                        self.heap[parent_index],
                        self.heap[last_index],
                    )
                    last_index = parent_index
                else:
                    # 스왑 안되면 명시적으로 탈출해주는게 좋다
                    break

    def pop(self):

        # 루트랑 마지막 원소 스왑
        last_index = len(self.heap) - 1

        if last_index < 0:
            return 0

        self.heap[0], self.heap[last_index] = (
            self.heap[last_index],
            self.heap[0],
        )

        pop_value = self.heap.pop()

        # 루트 제자리 찾기
        new_root_index = 0
        while True:

            left_child_index = 2 * new_root_index + 1
            right_child_index = 2 * new_root_index + 2

            # 자식이 두개인 경우
            if len(self.heap) > right_child_index:

                # 왼쪽이 더 크면 새로운 루트와 왼쪽 자식 스왑
                if self.heap[left_child_index] > self.heap[right_child_index]:

                    # 왼쪽 자식 크기 비교
                    if self.heap[new_root_index] < self.heap[left_child_index]:
                        self.heap[new_root_index], self.heap[left_child_index] = (
                            self.heap[left_child_index],
                            self.heap[new_root_index],
                        )
                        new_root_index = left_child_index
                    else:
                        break
                else:
                    # 오른쪽 자식 크기 비교
                    if self.heap[new_root_index] < self.heap[right_child_index]:
                        self.heap[new_root_index], self.heap[right_child_index] = (
                            self.heap[right_child_index],
                            self.heap[new_root_index],
                        )
                        new_root_index = right_child_index
                    else:
                        break
            # 자식이 하나인 경우
            elif len(self.heap) > left_child_index:
                if self.heap[new_root_index] < self.heap[left_child_index]:
                    self.heap[new_root_index], self.heap[left_child_index] = (
                        self.heap[left_child_index],
                        self.heap[new_root_index],
                    )
                    new_root_index = left_child_index
                else:
                    break
            # 더 이상 자식이 없는 경우
            else:
                break

        return pop_value


import sys

input = sys.stdin.readline

N = int(input().rstrip())
X = [int(input().rstrip()) for _ in range(N)]
max_heap = MyMaxHeap()

# N연산의 개수
# x = 0 이면 배열에서 가장 큰 값 출력 후 제거, 그 외엔 입력
# 최대 힙... 어떻게 생겨먹은 자료형이더라? 그냥 배열로 구현이 가능할텐데

for x in X:
    if x == 0:
        print(max_heap.pop())
    else:
        max_heap.push(x)
