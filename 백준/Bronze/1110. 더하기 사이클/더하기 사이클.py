n = int(input())
# x (x=n) -> a+b 로 만든다
# a = x/10, b = x%10
# a+b -> c 라고 하면
# 다음 x = b*10+c%10
cnt = 0
x = n
while(True):
    cnt += 1
    if x >= 10:
        a = x//10
        b = x%10
        c = a+b
        x = b*10 + c%10
    elif x < 10:
        x = x*10+x

    if x == n:
        break

print(cnt)
