N, S = map(int, input().split())
num_list = list(map(int, input().split()))


def combination(index, total):
    global count
    if index == N:
        if total == S:
            count += 1
        return
    combination(index + 1, total)
    combination(index + 1, total + num_list[index])


count = 0
combination(0, 0)

if S == 0:
    count -= 1

print(count)
