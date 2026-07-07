def solution(num_list, n):
    answer = []
    rows = len(num_list) // n
    for i in range(rows):
        answer.append(num_list[i * n:(i+1) * n])
    return answer