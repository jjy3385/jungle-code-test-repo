def solution(numlist, n):
    answer = sorted(numlist, key=lambda x: (abs(x-n), -1 * x))
    return answer