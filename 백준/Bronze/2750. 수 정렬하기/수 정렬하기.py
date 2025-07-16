import sys
N = int(sys.stdin.readline())
li = list(map(int,[sys.stdin.readline() for _ in range(N)]))
li.sort()
print("\n".join(map(str,li)))