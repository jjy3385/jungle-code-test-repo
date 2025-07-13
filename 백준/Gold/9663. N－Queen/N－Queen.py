N = int(input())

pos = [0] * N
flag_a = [False] * N
flag_b = [False] * (2 * N - 1)
flag_c = [False] * (2 * N - 1)

count = 0

def set(i: int) -> None:
    global count
    for j in range(N):
        if not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+N-1]:
            # print(f"진입: {i}열,{j}행에 퀸 놓기")
            pos[i] = j
            if i == N-1:
                count += 1
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+N-1] = True
                set(i + 1)
                # print(f"<- 백트래킹: {i}열,{j}행 해제")
                flag_a[j] = flag_b[i+j] = flag_c[i-j+N-1] = False
                # print("flag:",flag)
set(0)

print(count)