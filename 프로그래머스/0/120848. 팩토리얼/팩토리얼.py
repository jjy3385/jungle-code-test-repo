def solution(n):
    answer = 0
    fact = 1  
    for i in range(1,11):
        fact *= i
        if fact > n:
            answer = i - 1
            break
        elif fact == n:
            answer = i
            break
    
    return answer