
# sx = x좌표 오름차순 기준으로 정렬된 리스트
# sy = y좌표 오름차순 기준으로 정렬된 리스트
# left = 좌측 끝 인덱스
# right = 우측 끝 인덱스
def divide(left, right,strip):

    # base case
    # 케이스가 작아지면 직접 구해서 return
    # 갯수로 체크해야대

    if right - left <= 2:
        distance = sys.maxsize

        for i in range(left, right + 1):
            x0, y0 = sorted_X[i]
            for j in range(left, right + 1):
                x1, y1 = sorted_X[j]
                # 같은 좌표 제외
                if i != j:
                    distance = min(distance, ((x1 - x0) ** 2) + ((y1 - y0) ** 2))
        return distance

    mid = (left + right) // 2
    mid_x = sorted_X[mid][0]

    left_strip = [xy for xy in strip if xy[0] <= mid_x]
    right_strip = [xy for xy in strip if xy[0] > mid_x]

    # 왼쪽/오른쪽 분할하여 재귀호출
    left_distance = divide(left, mid,left_strip)
    right_distance = divide(mid + 1, right,right_strip)

    min_distance = min(left_distance, right_distance)

    # strip 처리

    # - min_distance < mid < min_distance 사이의 좌표들
    s_min_d = min_distance ** (1 / 2)
    strip_list = [xy for xy in strip if abs(xy[0] - mid_x) < s_min_d]

    for i in range(len(strip_list)):
        for j in range(i + 1, len(strip_list)):
            x0, y0 = strip_list[i]
            x1, y1 = strip_list[j]
            if (y1 - y0) ** 2 >= min_distance:
                break
            else:
                min_distance = min(min_distance, ((x1 - x0) ** 2) + ((y1 - y0) ** 2))

    return min_distance


import sys

input = sys.stdin.readline
N = int(input().rstrip())
XY = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
# x좌표 기준 오름차순 정렬
# 이거.. NlogN 이겠지??

sorted_X = sorted(XY, key=lambda x: x[0])
sorted_Y = sorted(XY, key=lambda x: x[1])

left = 0
right = N - 1

print(divide(left, right,sorted_Y))
