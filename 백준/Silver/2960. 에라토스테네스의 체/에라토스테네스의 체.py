N, K = map(int, input().split())

seive = [True] * (N + 1)
count = 0
for i in range(2,N+1):
    for j in range(i,N+1,i):
        if seive[j]:
            seive[j] = False
            count += 1
            if count == K:
                print(j)
        
