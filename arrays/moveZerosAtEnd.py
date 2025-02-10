
nums = [int(i) for i in input().split()]
res = []
for i in nums:
    if i != 0:
        res.append(i)
res = res + [0]*(len(nums)-len(res))
print(res)
