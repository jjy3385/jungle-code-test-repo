import math

def solution(numer1, denom1, numer2, denom2):
    total_denom = denom1 * denom2
    total_numer = (numer1 * denom2) + (numer2 * denom1)
    gcd = math.gcd(total_denom,total_numer)
    total_numer = total_numer / gcd    
    total_denom = total_denom / gcd
    answer = [total_numer,total_denom]
    
    return answer