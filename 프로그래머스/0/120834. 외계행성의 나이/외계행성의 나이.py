def solution(age):
    answer = ''
    for ch in str(age):
        answer += chr(ord(ch) + 49)
    return answer