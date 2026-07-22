def solution(score):
    answer = [0] * len(score)
    average = []
    
    # (원래 인덱스,점수합) 생성
    for i,v in enumerate(score):
        average.append((i,v[0] + v[1]))
    
    # 점수합 기준 내림차순정렬
    score = sorted(average,key = lambda x:-x[1])
    pre_average = score[0][1]
    ranking = 1    

    for i,s in enumerate(score): 
        # 동점은 등수 변화 X, 이후 등수는 score 인덱스 사용
        if pre_average != s[1]:
            ranking = i + 1
        # 원래 인덱스 위치에 등수 저장
        answer[s[0]] = ranking
        pre_average = s[1]
    
    return answer