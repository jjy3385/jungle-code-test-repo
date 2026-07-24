def solution(bin1, bin2):
    answer = ''
    length = max(len(bin1),len(bin2))
    bin1,bin2 = bin1.zfill(length),bin2.zfill(length)
    carry = 0
    for x,y in zip(bin1[::-1],bin2[::-1]):
        total = int(x) + int(y) + carry
        curr = total % 2
        carry = total // 2
        answer += str(curr)
    
    if carry:
        answer += str(carry)
    
    return answer[::-1]