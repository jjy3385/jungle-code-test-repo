for _ in range(int(input())):
    R, S = input().split()
    R = int(R)
    for c in S:
        print(c*R,end="")
    print()