import sys
import heapq
from collections import deque

input = sys.stdin.readline
# 테스트케이스의 수
T = int(input().rstrip())

for _ in range(T):

    # 문서의 개수 N
    # 현재 큐에서 몇번째로 인쇄될지 궁금한 문서의 인덱스 M
    N, M = list(map(int, input().rstrip().split()))
    priority = list(map(int, input().rstrip().split()))

    heap = []
    dq = deque()

    for i in range(N):
        # 우선순위,인덱스
        heapq.heappush(heap, -priority[i])
        dq.append((priority[i], i))

    count = 0
    while dq:

        first = dq.popleft()
        
        if first[0] != -heap[0]:
            dq.append(first)
        else:
            heapq.heappop(heap)
            count += 1

            if first[1] == M:
                break

    print(count)


# 그냥 큐에 순서대로 넣고 우선순위 큐에 우선순위에 맞춰서 넣어놓음
#
# print(priority)
# print(dq)
