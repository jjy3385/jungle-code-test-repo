def solution(n):
    answer = 0
    fact = 1  
    for i in range(1,11):
        fact *= i
        if fact > n:
            break
        answer = i
    return answer