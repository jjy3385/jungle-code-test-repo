def Z(N,r,c):

    count = 0
    while N:
        
        N -= 1
        # print(N)
        # 2사분면
        if r < 2 ** N and c < 2 ** N:
            count = count 

        # 1사분면
        elif r < 2 ** N and c >= 2 ** N:
            count += (2 ** N * 2 ** N)
            c -= 2 ** N

        # 3사분면
        elif r >= 2 ** N and c < 2 ** N:
            count += 2 * (2 ** N * 2 ** N)
            r -= 2 ** N
        # 4사분면
        elif r >= 2 ** N and c >= 2 ** N:
            count += 3 * (2 ** N * 2 ** N)
            c -= 2 ** N
            r -= 2 ** N

    return count

N,r,c = map(int,input().split())

print(Z(N,r,c))


