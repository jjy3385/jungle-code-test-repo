# 가지고 있는 숫자 카드의 개수 N
# 숫자 카드에 적혀있는 정수 cards - 상근이가 갖고 있는 수
# check_num 은 상근이가 갖고 있는지 확인해야하는 수

import sys

input = sys.stdin.readline
N = int(input().rstrip())
cards = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
check_num = list(map(int, input().rstrip().split()))

cards = sorted(cards)


def bsearch(target):

    result = False
    left = 0
    right = N - 1

    while left <= right:

        mid = (left + right) // 2

        if target == cards[mid]:
            result = True
            break
        elif target < cards[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return result


for i in range(M):
    if bsearch(check_num[i]):
        print(1, end=" ")
    else:
        print(0, end=" ")
