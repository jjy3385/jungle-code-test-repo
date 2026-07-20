def solution(my_string):
    answer = 0
    curr = ''
    for ch in my_string:
        if ch.isdigit():
            curr += ch
        else:
            if curr.isdigit():
                answer += int(curr)
            curr = ''
            
    if curr.isdigit():
        answer += int(curr)
        
    return answer