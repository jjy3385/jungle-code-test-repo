def solution(clothes):
    answer = 1
    dic = {}
    for name,kind in clothes:
        dic[kind] = dic.get(kind,0) + 1
    
    for count in dic.values():
        answer *= (count + 1)
    answer -= 1    
    return answer