def solution(lines):
    answer = 0
    for i in range(-100,100):
        temp = 0 
        for l in lines:
            if l[0] <= i < l[1]:
                temp += 1
            if temp >= 2:
                answer += 1
                break
    return answer