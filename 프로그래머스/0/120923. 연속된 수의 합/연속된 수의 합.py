def solution(num, total):
    answer = []
    x = (total - ((num * (num - 1)) / 2)) / num
    print(x)
    for i in range(num):
        answer.append(x + i)
    return answer