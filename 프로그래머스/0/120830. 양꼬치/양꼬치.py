def solution(n, k):
    answer = n * 12000
    answer += k * 2000
    answer -= (n // 10) * 2000
    return answer