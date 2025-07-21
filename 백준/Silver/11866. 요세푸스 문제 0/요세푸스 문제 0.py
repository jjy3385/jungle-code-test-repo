import sys

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

queue = [i for i in range(1, N + 1)]
result = []
index = 0

while len(queue) > 0:
    # 배열이 한칸 줄어듬 + #3칸 진행
    index += K - 1
    index = index % len(queue)
    result.append(queue.pop(index))

print(f"<{', '.join(map(str,result))}>")
