def solution(n):
    a = n
    b = 6
    while b != 0:
        a, b = b, a % b
    
    lcm = int(6 * n / a)
    print()
    
    
    answer = lcm / 6
    return answer