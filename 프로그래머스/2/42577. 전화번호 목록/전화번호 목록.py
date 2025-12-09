def solution(phone_book):
    answer = True
    s = set()
    for num in phone_book:
        s.add(num)

    for num in phone_book:
        for n in range(1,len(num)):
            prefix = num[:n]
            if prefix in s:
                return False
    return answer