def solution(sides):
    answer = 0
    x = max(sides)
    y = min(sides)
    # 가장 긴 변이 x인 경우
    for i in range(x + 1):
        if i + y > x:
            answer += 1
    # 나머지 한변이 가장 긴 경우            
    for i in range(x + 1,x + y):
        if x + y > i:
            answer += 1
    return answer