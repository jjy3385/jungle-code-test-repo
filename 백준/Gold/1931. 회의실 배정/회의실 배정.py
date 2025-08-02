import sys

input = sys.stdin.readline

N = int(input().rstrip())
meetings = sorted(
    [tuple(map(int, input().rstrip().split())) for _ in range(N)],
    key=lambda x: (x[1], x[0]),
)

res = []
res.append(meetings[0])
for i in range(1,N):
    prev_start,prev_end = res[-1]
    now_start,now_end = meetings[i]

    if prev_end <= now_start:
        res.append((now_start,now_end))
    

print(len(res))