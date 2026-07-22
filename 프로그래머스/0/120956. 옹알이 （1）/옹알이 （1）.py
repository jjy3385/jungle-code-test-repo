def solution(babbling):
    answer = 0
    possible_list = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        while b != '':
            found = False
            for p in possible_list:
                if p == b[:len(p)]:
                    b = b[len(p):]
                    found = True
                    break
                    
            if b == '':
                answer += 1
                
            # 옹알이를 못찾으면 while break    
            if found == False:
                break
    return answer