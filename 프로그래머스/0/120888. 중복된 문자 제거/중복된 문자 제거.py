def solution(my_string):
    dup = []
    for ch in my_string:
        if ch not in dup:
            dup.append(ch)
    answer = ''.join(dup)
    return answer