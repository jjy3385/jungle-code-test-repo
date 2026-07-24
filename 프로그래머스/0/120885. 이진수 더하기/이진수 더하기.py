def solution(bin1, bin2):
    answer = ''
    i = len(bin1) - 1
    j = len(bin2) - 1
    carry = 0
    curr = 0
    while i >= 0 or j >= 0 or carry:
        bin1_temp = 0
        bin2_temp = 0        
        if i >= 0 and bin1[i] == '1':
            bin1_temp = 1
        if j >= 0 and bin2[j] == '1':
            bin2_temp = 1
            
        if bin1_temp + bin2_temp + carry == 3:
            carry = 1
            curr = 1
        elif bin1_temp + bin2_temp + carry == 2:
            carry = 1
            curr  = 0
        elif bin1_temp + bin2_temp + carry == 1:
            carry = 0
            curr  = 1
        else:
            carry = 0
            curr  = 0
            
        answer = str(curr) + answer   
            
        i -= 1
        j -= 1
        
    return answer