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
    minus,plus = num//2,num//2
    while True:
        if is_prime(minus) and is_prime(plus):
            break
        minus -= 1
        plus += 1 
    print(minus,plus)