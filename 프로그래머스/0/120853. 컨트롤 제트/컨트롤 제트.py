def solution(s):
    answer = 0
    before = 0
    for ch in s.split():
        if ch == 'Z':
            answer -= int(before) 
        else:
            answer += int(ch)
            before = int(ch)
    return answer