def solution(a, b):
    answer = 2
    b = b // gcd(a,b)
    
    while b != 1 and b % 2 == 0:
        b = b // 2
        
    while b != 1 and b % 5 == 0:
        b = b // 5
    
    if b == 1:
        answer = 1
        
    return answer

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
