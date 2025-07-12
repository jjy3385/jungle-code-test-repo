x,y = map(int,input().split())
cnt = int(input())
x_cut,y_cut = [0,x],[0,y]
for _ in range(cnt):
    isY,num = map(int,input().split())
    if isY:
        x_cut.append(num)
    else:
        y_cut.append(num)

x_cut = sorted(x_cut)
y_cut = sorted(y_cut)

max_x = max([x_cut[i+1] - x_cut[i] for i in range(len(x_cut) - 1)])
max_y = max([y_cut[i+1] - y_cut[i] for i in range(len(y_cut) - 1)])

print(max_x * max_y)