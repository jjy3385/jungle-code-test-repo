def solution(numbers, direction):
    answer = []
    lastIdx = len(numbers) - 1
    if direction == "right":
        answer.append(numbers[lastIdx])
        for i in range(lastIdx):
            answer.append(numbers[i])
    else:
        for i in range(1,lastIdx+1):
            answer.append(numbers[i])  
        answer.append(numbers[0])
    return answer