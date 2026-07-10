def solution(cipher, code):
    answer = ''.join(v for i,v in enumerate(cipher,1) if i % code == 0)
    return answer