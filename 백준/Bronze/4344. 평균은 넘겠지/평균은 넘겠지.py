for _ in range(int(input())):
    N,*scores = map(int,input().split())
    avg = sum(scores) / N
    cnt = 0
    for s in scores:
        if s > avg:
            cnt += 1
    print(f"{cnt/N:.3%}")