
import sys

input = sys.stdin.readline

# 멀티탭 구멍의 개수 N, 전기 용품의 총 사용횟수 K
N, K = map(int, input().rstrip().split())
# 전기용품의 이름 + 사용순서
orders = list(map(int, input().rstrip().split()))

# 샘플
# 2 10
# 1 2 3 2 3 1 4 2 1 3

socket = set()
cnt = 0

for i in range(K):
    item = orders[i]

    # 이미 있으면 패스
    if item in socket:
        # print(f"이미 있으면 패스 item = {item}, socket = {socket}")
        continue

    # 콘센트에 여유가 있으면 그냥 꽂음
    if len(socket) < N:
        socket.add(item)
        # print(f"빈자리에 꽂음 item = {item}, socket = {socket}")
        continue

    # 제거할 item 선택
    # 가장 나중에 쓰이는 기기가 선택됨
    lastest_idx = -1
    to_remove = -1

    for s in socket:
        try:
            next_use = orders[i + 1 :].index(s)
            # print(f"빈자리에 꽂음 item = {item}, socket = {socket}")

        except ValueError:
            # 앞으로 안쓰이면 바로 제거
            to_remove = s
            break
        else:
            # try 에서 예외가 발생하지 않으면 실행
            if next_use > lastest_idx:
                lastest_idx = next_use
                to_remove = s

    socket.remove(to_remove)
    socket.add(item)
    cnt += 1


print(cnt)
