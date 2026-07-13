def solution(s1, s2):
    answer = 0
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                answer += 1
    return answer