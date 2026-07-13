def solution(my_string):
    answer = sum(int(ch) for ch in my_string.replace(' - ',' + -').split(' + '))
    return answer