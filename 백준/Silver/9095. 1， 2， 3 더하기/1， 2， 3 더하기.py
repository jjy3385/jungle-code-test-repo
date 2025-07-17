import sys

sys.setrecursionlimit(10**6)
T = int(input())
nums = [int(input()) for _ in range(T)]

coins = [1, 2, 3]

def get_coins(num, remain):
    global count 
    # base case
    if sum(paths) >= num:
        if sum(paths) == num: 
            # print(f"num = {num},paths = {paths}")    
            count += 1

        return

    for i in range(3):
        paths.append(coins[i])
        # print(paths)
        get_coins(num, remain - coins[i])
        paths.pop()

for i in range(T):
    paths = []
    count = 0
    get_coins(nums[i], nums[i])
    print(count)


