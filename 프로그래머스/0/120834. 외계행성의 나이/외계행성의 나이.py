def solution(age):
    answer = ''
    for ch in str(age):
        # '0' 은 48, 'a' 는 97
        answer += chr(ord(ch) + 49)
    return answer