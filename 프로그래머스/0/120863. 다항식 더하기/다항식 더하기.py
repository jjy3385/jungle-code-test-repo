def solution(polynomial):
    answer = ''
    a,b = 0,0
    for p in polynomial.split(' '):
        if 'x' == p:
            a += 1
        elif 'x' in p:
            a += int(p.replace('x',''))
        elif p != '+':
            b += int(p)
    if a > 0:
        answer += str(a) + 'x' if a > 1 else 'x'
    if b > 0:
        answer += ' + ' + str(b) if a > 0 else str(b)
        
    return answer