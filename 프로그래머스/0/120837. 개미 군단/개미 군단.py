def solution(hp):
    answer = hp // 5
    remain = hp % 5
    answer += remain // 3
    remain = remain % 3
    answer += remain
    return answer