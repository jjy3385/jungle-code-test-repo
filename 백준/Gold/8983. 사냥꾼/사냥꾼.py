
# 발사대의 수 M
# 동물의 수 N
# 사정거리 L
import sys

input = sys.stdin.readline
M, N, L = map(int, input().rstrip().split())
# 사대의 X 위치
X = sorted(list(map(int, input().rstrip().split())))
# N마리 동물의 좌표
animals = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
# 사대의 위치X 와 동물의 위치 (a,b) 간의 거리공식
# abs(X - a) + b
# 잡을 수 있는 동물의 수를 음수가 아닌 정수로 출력


# 해당 좌표의 동물이 잡을 수 있는지 확인(T/F)
def bsearch(animal):
    a, b = animal
    start = 0
    end = M - 1
    result = False

    while start <= end:

        mid = (start + end) // 2
        # print(f"animal = {animal}, start = {start}, end = {end}, mid = {mid}")
        if abs(X[mid] - a) + b <= L:
            result = True
            break
        else:
            if X[mid] < a:
                start = mid + 1
            elif X[mid] > a:
                end = mid - 1
            else:
                result = False
                break
    return result


count = 0
for animal in animals:
    if bsearch(animal):
        # print(animal)
        count += 1

print(count)
