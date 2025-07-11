max,count = 0,0
for i in range(9):
    num = int(input())
    if max < num:
        max = num
        count = i+1
print(max)
print(count)

    