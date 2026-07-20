def solution(spell, dic):
    answer = 2
    spell = ''.join(sorted(spell))
    dic = map(sorted,dic)
    for d in dic:
        if ''.join(d) == spell:
            answer = 1
            break
        
    return answer