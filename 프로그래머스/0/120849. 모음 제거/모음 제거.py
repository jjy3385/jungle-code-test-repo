def solution(my_string):
    answer = ''
    v = ['a','e','i','o','u']
    for ch in my_string:
        if ch not in v:
            answer += ch
    return answer