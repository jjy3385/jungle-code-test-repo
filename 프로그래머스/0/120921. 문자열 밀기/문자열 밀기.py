def solution(A, B):
    answer = -1
    length = len(A)
    for i in range(length):
        if A == B:
            answer = i
            break
        A = A[::-1][0] + A[:len(A)-1]
    return answer