# Intersection of Two Arrays

# Problem: Write a function that returns the common elements between two arrays.
# Testcase 1:
# Input: [1, 2, 3], [2, 3, 4]
# Output: [2, 3]

arr1=[1,2,3,]
arr2=[2,4,5]
res=[]
for i in arr1:
    if i in arr2 and i not in res:
        res+=[i]
print(res)