a = int(input())
b = int(input())
sum = 0
for i in range(3):
    digit = b % 10
    print(a * digit)
    sum += a * digit * (10 ** i)
    b //= 10
print(sum)
