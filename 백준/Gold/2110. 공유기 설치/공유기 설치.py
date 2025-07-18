import sys

input = sys.stdin.readline

N, C = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])

# 파라메트릭 서치
# 좌표나 요소를 찾는게 아니라 최적화 값을 찾아가는 이분탐색


# 조건에 만족하는 거리인가?
# 리스트 내 집에 C개의 공유기를 설치할 수 있는가?
def can_install(distance):
    count = 1
    last = A[0]
    for i in range(1, N):
        if A[i] - last >= distance:
            count += 1
            last = A[i]
    return count >= C


start = 1  # 최소 가능한 거리
end = A[-1] - A[0]  # 최대 가능한 거리
answer = 0  # 두 공유기 사이의 최대 거리

# 최소 가능한 거리에서 최대가능한 거리까지
while start <= end:
    mid = (start + end) // 2

    if can_install(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
