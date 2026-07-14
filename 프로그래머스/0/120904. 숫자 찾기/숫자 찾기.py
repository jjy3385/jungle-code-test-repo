def solution(num, k):
    answer = -1
    for i,v in enumerate(str(num)):
        if k == int(v):
            answer = i + 1
            break
    return answer