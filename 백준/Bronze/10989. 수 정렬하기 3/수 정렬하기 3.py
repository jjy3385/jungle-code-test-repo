import sys
N = int(sys.stdin.readline())
ls = [0] * 10001
for _ in range(N):
    ls[int(sys.stdin.readline())] += 1
for i in range(1,10001):
    for j in range(ls[i]):
        sys.stdout.write(f'{i}\n')