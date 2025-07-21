import sys

input = sys.stdin.readline

N = int(input().rstrip())
towers_list = list(map(int, input().rstrip().split()))
towers = list(enumerate(towers_list, start=1))


res = [0] * N
stack = []

for i in range(N):
    idx,height = towers[i]

    # 스택이 비지 않았고 현재 높이 > 스택top 이면 pop()으로 제거
    # 이미 현재높이보다 낮은 왼쪽 탑들인 이제 쓸모가 없음 
    while stack and stack[-1][1] < height:
        stack.pop()
    
    # 스택에 남아 있다는 건 현재 높이 > 이전 탑 높이
    if stack:
        res[i] = stack[-1][0]
    
    # 즉 스택에는 매번 넣고 있음
    # 다만 반복에 현재 높이보다 낮으면 제거되는 구조
    stack.append((idx,height))

print(" ".join(map(str, res)))