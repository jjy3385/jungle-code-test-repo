a,b = input().split()
x,y = '',''
for i in range(2,-1,-1):
    x += a[i]
    y += b[i]
print(max(int(x),int(y)))
