N = int(input())
count = 0

for i in range(1,N+1):
    if i < 100:
        count += 1
    elif i < 1000:
        # i가 한수면  count + 1
        s = str(i)
        if int(s[1]) - int(s[0]) == int(s[2]) - int(s[1]):
            count += 1
print(count)