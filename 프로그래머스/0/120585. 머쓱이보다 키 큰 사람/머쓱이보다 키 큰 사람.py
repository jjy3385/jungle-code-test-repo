def solution(array, height):
    answer = 0
    array.append(height)
    for i,v in enumerate(sorted(array, reverse=True)):
        if height == v:
            answer = i
            break
    return answer