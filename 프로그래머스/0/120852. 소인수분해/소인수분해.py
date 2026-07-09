def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)  
            while n % i == 0: 
                n //= i
                
        i += 1   
        
    return answer