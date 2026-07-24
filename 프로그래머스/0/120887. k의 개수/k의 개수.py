def solution(i, j, k):
    answer = 0
    sk = str(k)
    for x in range(i,j + 1):        
        if sk in str(x):
            answer += str(x).count(sk)
    return answer