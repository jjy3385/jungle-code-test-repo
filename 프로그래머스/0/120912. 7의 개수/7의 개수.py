def solution(array):
    # return ''.join(str(n) for n in array).count('7')
    return ''.join(map(str,array)).count('7')