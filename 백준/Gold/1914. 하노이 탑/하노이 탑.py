N = int(input())

# 시작지,목적지,원판의 개수
def hanoi(start,mid,end,num):
    if num == 1:
        print(start,end)
        return
    hanoi(start,end,mid,num-1)
    print(start,end)
    hanoi(mid,start,end,num-1)

print((1<<N)-1)
if N <= 20:
    hanoi('1','2','3',N)