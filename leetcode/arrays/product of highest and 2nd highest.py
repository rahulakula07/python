# Find the Maximum Product of Two Elements

# Problem: Write a function to find the maximum product of two elements in an array.
# Testcase 1:
# Input: [3, 5, -2, 8, 11]
# Output: 8 * 11 → 88

arr=[3,4,-2,8,11]
res=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] < arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr[0]*arr[1])