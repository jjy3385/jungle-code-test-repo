import sys
input=sys.stdin.readline

n=input().rstrip()
key=input().rstrip()
kk=[]
for i in key:
    kk.append(i)

cnt=len(key)
stack=[]


for i in n:
    stack.append(i)
    # print(stack)
    if stack[-cnt:] == kk:
        for j in range(cnt):
            stack.pop()
            # print(stack)
            if not stack:
                break

if not stack:
    print('FRULA')
else:
    for i in stack:
        print(i,end='')