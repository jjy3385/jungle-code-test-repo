def solution(a, b):
    b = b // gcd(a,b)
    
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5

    if b == 1:
        return 1
    return 2

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
