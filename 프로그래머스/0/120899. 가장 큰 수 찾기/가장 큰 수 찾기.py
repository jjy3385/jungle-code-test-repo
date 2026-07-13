def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(answer[0]))
    return answer