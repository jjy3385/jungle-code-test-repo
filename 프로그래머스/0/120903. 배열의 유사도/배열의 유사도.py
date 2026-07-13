def solution(s1, s2):
    answer = 0
    for e1 in s1:
        if e1 in s2:
            answer += 1
    return answer