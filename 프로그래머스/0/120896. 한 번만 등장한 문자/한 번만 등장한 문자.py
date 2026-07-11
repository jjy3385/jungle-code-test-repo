def solution(s):
    answer = ''.join([ch for ch in sorted(s) if s.count(ch) == 1])
    return answer