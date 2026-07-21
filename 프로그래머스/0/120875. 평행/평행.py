def solution(dots):
    answer = 0
    if isPallel(dots,0,1,2,3) or isPallel(dots,0,2,1,3) or isPallel(dots,0,3,1,2):
        answer = 1
    return answer

def isPallel(dots,a,b,c,d):
    dy1 = dots[a][1] - dots[b][1]
    dx1 = dots[a][0] - dots[b][0]
    dy2 = dots[c][1] - dots[d][1]
    dx2 = dots[c][0] - dots[d][0]
    if dy1 * dx2 == dy2 * dx1:
        return True
    return False