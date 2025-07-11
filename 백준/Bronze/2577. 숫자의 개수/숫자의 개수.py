a = [0] * 10
M = str(int(input()) * int(input()) * int(input()))
for c in M:
    a[int(c)] += 1
for n in a:
    print(n)