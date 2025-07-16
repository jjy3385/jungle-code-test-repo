import sys
T = int(sys.stdin.readline())

li = []
for _ in range(T):
    li.append(int(sys.stdin.readline()))

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(T):
    half = li[i]//2
    for j in range(half):
        if is_prime(half-j) and is_prime(half+j):
            print(f"{half-j} {half+j}")
            break