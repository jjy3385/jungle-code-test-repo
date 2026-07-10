def solution(my_string):
    answer = ''.join([ch.swapcase() for ch in my_string])
    return answer