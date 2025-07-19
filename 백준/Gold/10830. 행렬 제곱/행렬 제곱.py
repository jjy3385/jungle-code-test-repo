import sys

input = sys.stdin.readline
N, B = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(N)]


# 행렬의 크기 N , 행렬 A를 B 제곱해라
# 각 원소는 1000으로 나눈 나머지를 출력


# 1.항등행렬 I
def identity():

    I = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                I[i][j] = 1
            else:
                I[i][j] = 0
    return I


# 2.행렬의 곱셈 함수
# C[i][j] += A[i][k] * B[k][j]
# 이게 왜 되지?
# 반복문 따라가보니 되는거 맞긴한데 ... 원리는 모르겠고 그냥 외워야 될듯
def multi_maxtrix(a, b):
    c = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] += a[i][k] * b[k][j]

    # mod 연산 적용
    for i in range(N):
        for j in range(N):
            c[i][j] = c[i][j] % 1000

    return c


def squaring(a, b):

    # print(a, b)

    if b == 0:
        return identity()

    if b == 1:
        # mod 연산 전부 적용해줘야함
        return [[x % 1000 for x in li] for li in a]

    half = squaring(a, b // 2)

    if b % 2 == 0:
        return multi_maxtrix(half, half)
    else:
        return multi_maxtrix(a, multi_maxtrix(half, half))


res = squaring(A, B)

for i in range(N):
    for j in range(N):
        print(res[i][j], end=" ")
    print()
