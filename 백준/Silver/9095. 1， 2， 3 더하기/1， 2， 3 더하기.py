lst = [1,2,3]
t = int(input())

cnt = 0
def perm(n):
    def dfs(total):
        global cnt
        if total > n:
            return
        if total == n:
            cnt += 1
            return

        for i in range(3):
            dfs(total+lst[i])
    dfs(0)


for i in range(t):
    n = int(input())
    perm(n)
    print(cnt)
    cnt = 0
