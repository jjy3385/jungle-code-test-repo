from math import factorial
def solution(balls, share):
    answer = factorial(balls) / (factorial(balls-share) * factorial(share))
    return answer