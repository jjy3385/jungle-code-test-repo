N = int(input())
for i in range(N):
    OX = input()
    sum, score = 0, 0
    for c in OX:
        if c == "O":
            score += 1
            sum += score
        else:
            score = 0
    print(sum)
