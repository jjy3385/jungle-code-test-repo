def solution(emergency):
    arr = sorted(emergency,reverse=True)
    dict = {v:i for i,v in enumerate(arr,start=1)}
    answer = [dict[e] for e in emergency]
    return answer