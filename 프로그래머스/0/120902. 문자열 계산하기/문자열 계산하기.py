def solution(my_string):
    answer = 0
    s = my_string.split(" ")
    op = '+'
    for ch in s:
        if ch in ['+','-']:
            op = ch
        else:
            if op == '-':
                answer -= int(ch)
            else:
                answer += int(ch)
        
    return answer