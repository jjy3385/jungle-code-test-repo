import sys

input = sys.stdin.readline

expr = input().rstrip()

# 마이너스가 들어오면 자른다
# 일단 다 자른다

nums = expr.split("-")
# print(nums)
res = []
for n in nums:
    temp_sum = 0
    for i in n.split('+'):
        temp_sum += int(i)
    res.append(temp_sum)

print(res[0] - sum(res[1:]))