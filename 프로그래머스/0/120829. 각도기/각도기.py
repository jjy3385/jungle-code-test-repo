
def solution(angle):
    answer = 0
    if angle <= 90:
        answer = 1 if angle < 90 else 2
    else:
        answer = 3 if angle < 180 else 4
    return answer