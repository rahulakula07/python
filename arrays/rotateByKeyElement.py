#rotate array by k elements by right side

nums = input().split()  # 10 20 30 40 50 60 70
k = int(input())
for i in range(k):
    last = nums[-1]
    for j in range(len(nums)-2,-1,-1):
        nums[j+1] = nums[j]
    nums[0] = last
    # print(nums, i+1)
print(* nums)