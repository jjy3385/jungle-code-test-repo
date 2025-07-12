T = int(input())
A = []
for i in range(T):
    A.append(int(input()))

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in A:
    half = int(num/2)
    plus = half
    minus = half
    while True:
        if is_prime(plus) and is_prime(minus):
            break
        plus += 1
        minus -= 1
    print(minus,plus)