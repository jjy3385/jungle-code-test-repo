def solution(array, n):
    answer = 100
    distance = 100
    array.sort()
    for a in array:
        if abs(n - a) < distance:
            distance = abs(n - a)
            answer = a
    return answer