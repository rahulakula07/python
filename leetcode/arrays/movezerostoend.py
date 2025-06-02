# Move Zeros to End

# Problem: Write a function that moves all zeros in an array to the end while maintaining the order of other elements.
# Testcase 1:
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]


arr=[0, 1, 0, 3, 12]
res=[]
for i in arr:
    if i!=0:
        res+=[i]
res+=[0]*(len(arr)-len(res))
print(res)