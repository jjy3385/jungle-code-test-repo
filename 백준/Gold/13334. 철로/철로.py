import sys
import heapq


input = sys.stdin.readline
N = int(input().rstrip())
# 집/사무실 위치
ho = [sorted(map(int, input().rstrip().split())) for _ in range(N)]
# 철로의 길이
length = int(input().rstrip())

# 집/사무실 위치 정렬
# 영역끝점 기준으로 오름차순 정렬
interval = sorted(ho, key=lambda x: x[1])

# print(interval)
heap = []
count = 0
for i in range(N):
    start, end = interval[i]
    rail_start = end - length
    # print(start,end)
    #  현재 영역 시작 >= 현재 영역 끝 - 철로길이
    # 즉, 집과 사무실의 거리가 유효한 경우에만 push
    if start >= rail_start:
        heapq.heappush(heap, start)

    # 최소힙에서 제거되어야 하는 위치 탐색하여 제거
    while heap and heap[0] < rail_start:
        heapq.heappop(heap)

    count = max(count, len(heap))

print(count)
