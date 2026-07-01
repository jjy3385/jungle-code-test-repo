def solution(emergency):
    arr = sorted(emergency,reverse=True)
    rank = {v:i for i,v in enumerate(arr,start=1)}
    answer = [rank[e] for e in emergency]
    return answer