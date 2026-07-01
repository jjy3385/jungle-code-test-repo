def solution(emergency):
    answer = []
    arr = sorted(emergency,reverse=True)
    dict = {}
    for i,v in enumerate(arr,start=1):
        dict[v] = i
    for e in emergency:
        answer.append(dict[e])
    return answer