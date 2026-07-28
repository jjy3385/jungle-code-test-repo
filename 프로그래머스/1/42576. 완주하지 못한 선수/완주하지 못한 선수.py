def solution(participant, completion):
    answer = ''
    count = {}
    for p in participant:
        count[p] = count.get(p,0) + 1
    
    for name in completion:
        count[name] -= 1
    
    for n,c in count.items():
        if c == 1:
            return n
    return answer