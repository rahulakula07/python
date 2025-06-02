# Find Missing Number

# Problem: Given an array of consecutive numbers with one missing, find the missing number.
# Testcase 1:
# Input: [1, 2, 4, 5]
# Output: [3]

arr=[10,11,12,14]
res=[]
for i in range(arr[0],arr[-1]+1):
    # print(arr)
    if i not in arr:
        res+=[i]
print(res)
        