import sys
input = sys.stdin.readline

n=int(input())
n_card = list(map(int, input().split()))
m=int(input())
m_card = list(map(int, input().split()))

n_card.sort()

a=[0]*m

def sol(start, end, i):

    while start < end:
        mid = (start + end) //2

        if  n_card[mid] == m_card[i]:
            a[i] = 1
            return
        elif n_card[mid] > m_card[i]:
            end = mid
        else:
            start = mid + 1


for i in range(m):
    sol(0, n, i)

for i in a:
    print(i, end=' ')