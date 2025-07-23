# import sys
# import heapq


# input = sys.stdin.readline
# N = int(input().rstrip())
# circles = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

# interval = []
# for c in circles:
#     x, r = c
#     interval.append((x - r, x + r))

# # 끝점(x + r) 기준으로 오름차순 정렬
# # 가장 왼쪽 원부터 차례로 검사
# interval = sorted(interval, key=lambda x: x[1])

# heap = []
# count = 1

# for i in range(N):
#     start, end = interval[i]
#     length = end - start
#     is_full = False
#     last_end = end

#     while heap:

#         # print(f"heap = {heap}")
#         e, l = heapq.heappop(heap)
#         e = -e
#         # 이전 원 끝점 <= 현재 원 시작 -> 그대로 큐에 삽입
#         if e <= start:
#             heapq.heappush(heap, (-e, l))
#             break

#         if e != last_end and e - l >= start:
#             continue

#         # 이전 원 시작점 >= 현재 원 시작
#         if e - l >= start:
#             last_end = e - l

#         # 현재 원이 내부원의 원들로 꽉 찬 경우
#         if last_end == start:
#             is_full = True
#     count += 1
#     if is_full:
#         count += 1
#     # 끝점이 가장 오른쪽에 있는 원부터 검사할 수 있게 최대힙으로 구성
#     # 최대힙처럼 쓰기 위해 음수처리
#     heapq.heappush(heap, (-end, length))

# print(count)

# 스택을 이용한 다른 풀이 (GPT)


# import sys

# input = sys.stdin.readline
# N = int(input().rstrip())
# circles = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

# interval = []
# for c in circles:
#     x, r = c
#     interval.append((x - r, x + r))

# # 끝점(x + r) 기준으로 오름차순 정렬
# # 가장 왼쪽 원부터 차례로 검사
# interval = sorted(interval, key=lambda x: x[1])

# # 바깥 영역이 있기 때문에 기본값 = 1
# count = 1
# stack = []

# for start, end in interval:
#     last_end = end

#     while stack:
#         prev_start, prev_end = stack[-1]

#         # 1.겹치지 않음
#         # stack 에 있는 원과 현재 원이 겹치지 않음
#         # 그냥 while 종료
#         if prev_end <= start:
#             break

#         # 2.stack 에 있는 원이 현재 원을 포함하고 있음
#         # 안에 또 원이 있는지 검사 필요 -> stack.pop()
#         if prev_start > start:
#             last_end = prev_start
#             stack.pop()
#         else:
#             break

#     # 그냥 그리기만 해도 + 1
#     count += 1

#     # 현재 원을 내부원들이 꽉 채웠으면 + 1
#     if last_end == start:
#         count += 1

#     stack.append((start, end))

# print(count)


# 이것도 이해가 잘가진 못하고 답도 안나옴...


import sys
import heapq

input = sys.stdin.readline
N = int(input().rstrip())
circles = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

interval = []
for c in circles:
    x, r = c
    interval.append((x + r, 2 * r))

# 끝점(x + r) 기준으로 오름차순 정렬
# 가장 왼쪽 원부터 차례로 검사
interval.sort()

count = 1
heap = []

# print(interval)

for i in range(N):
    # 해당 원의 시작,끝점
    end, length = interval[i]
    # 해당 원이 그리는 영역의 길이
    start = end - length
    # 해당 원이 다른 원으로 꽉 찼는지 여부
    is_full = False

    last_end = end

    while heap:

        prev_end, prev_length = heapq.heappop(heap)
        # 최대힙처럼 쓰기 위해 음수처리한 부분 원래대로 돌림
        prev_end = -prev_end
        prev_start = prev_end - prev_length

        # 이전 원의 끝점 <= 현재 원의 시작점
        # 특이사항 X
        # 꺼냈던 이전 원을 큐에 다시 삽입
        if prev_end <= start:
            heapq.heappush(heap, (-prev_end, prev_length))
            break

        # 큐의 원이 현재 원에 들어가있지만 완전히 채우진 못한 경우
        if prev_end != last_end and prev_start >= start:
            continue

        # 큐의 원 시작점 >= 현재 원 시작점
        # 즉, 큐의 원이 현재원에 들어가 있음
        if prev_start >= start:
            last_end = prev_start

        # 큐에서 pop()을 진행하면서 이전 원의 시작점을 계속 남기던 last_end 가 현재 원의 start 와 같아지면
        # 전체가 꽉 찬 것으로 볼 수 있음
        if last_end == start:
            is_full = True

    # 원 추가 시 마다 영역 + 1
    count += 1

    if is_full:
        count += 1

    # 끝점이 가장 오른쪽에 있는 원이 맨 앞에 오도록 우선순위 큐에 삽입(최대힙)
    heapq.heappush(heap, (-end, length))

    # print(heap)

print(count)
