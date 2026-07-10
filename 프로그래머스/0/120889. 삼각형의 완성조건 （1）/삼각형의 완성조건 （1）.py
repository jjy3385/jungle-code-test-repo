def solution(sides):
    sides.sort()  
    answer = 2 if sides[2] >= sides[0] + sides[1] else 1
    return answer