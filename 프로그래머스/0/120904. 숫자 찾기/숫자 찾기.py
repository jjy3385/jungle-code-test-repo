def solution(num, k):
    answer = -1
    for i,v in enumerate(str(num)):
        if k == int(v):
            return i + 1
    return answer