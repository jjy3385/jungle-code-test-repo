N = int(input())
visited = [False] * N
daegak_1 = [False] * (2 * N - 1)
daegak_2 = [False] * (2 * N - 1)
count = 0

def queen(i):
    global count
    # base case
    if i == N:
        count += 1
        return
    
    for j in range(N):
        if not visited[j] and not daegak_1[i+j] and not daegak_2[i-j+N-1]:
            visited[j] = daegak_1[i+j] = daegak_2[i-j+N-1] = True
            queen(i+1)           
            visited[j] = daegak_1[i+j] = daegak_2[i-j+N-1] = False

queen(0)
print(count)
            