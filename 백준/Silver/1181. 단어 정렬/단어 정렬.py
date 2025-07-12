N = int(input())
ls = []
for _ in range(N):
    ls.append(input())
ls = list(set(ls))    
ls.sort()
ls.sort(key=len)
print("\n".join(ls))
