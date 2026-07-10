def solution(order):
    answer = sum([1 for ch in str(order) if ch in ['3','6','9']])
    return answer