def solution(quiz):
    answer = []
    for q in quiz:
        arr = q.split(' ')
        x = int(arr[0])
        y = int(arr[2])
        z = int(arr[4])
        o = arr[1]
        if o == "+":
            if z == x + y:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if z == x - y:
                answer.append("O")
            else:
                answer.append("X")
    return answer