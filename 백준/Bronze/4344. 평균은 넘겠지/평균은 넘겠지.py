C = int(input())
for _ in range(C):
    N,*scores = map(int,input().split())
    sum,cnt = 0,0
    for s in scores:
        sum += s
    avg = sum / N
    for s in scores:
        if s > avg:
            cnt += 1
    print(f"{cnt/N:.3%}")