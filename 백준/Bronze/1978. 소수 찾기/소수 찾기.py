N = int(input())
L = map(int,input().split())
count = 0

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for x in L:
    if(is_prime(x)):
        count+= 1
print(count)