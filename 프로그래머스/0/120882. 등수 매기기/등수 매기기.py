def solution(score):
    answer = [0] * len(score)
    average = []
    
    for i,v in enumerate(score):
        average.append((i,v[0] + v[1]))
    
    score = sorted(average,key = lambda x:-x[1])
    pre_average = score[0][1]
    ranking = 1    

    for i,s in enumerate(score): 
        print(i,s)
        if pre_average != s[1]:
            ranking = i + 1
        
        answer[s[0]] = ranking
        pre_average = s[1]
    
    return answer