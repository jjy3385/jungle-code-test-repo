import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())

# 1 ~ N 이 적힌 card 리스트
cards = [i for i in range(1, N + 1)]
queue = deque(cards)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())


print(queue.popleft())
