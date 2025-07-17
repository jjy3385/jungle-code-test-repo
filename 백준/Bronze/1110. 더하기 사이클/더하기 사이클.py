N = input()
if len(N) == 1:
    N = "0" + N    

cycle = 0
num = N
while True:
    temp = int(num[0]) + int(num[1])
    if temp < 10:
        temp = "0" + str(temp)    
    # print(temp)
    num = num[1] + str(temp)[1]
    cycle += 1
    # print(f"num: {num}, cycle: {cycle}")
    if num == N:
        break
print(cycle)
