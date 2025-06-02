# Rotate an Array

# Problem: Write a function that rotates an array to the right by a given number of steps.
# Testcase 1:
# Input: [1, 2, 3, 4, 5], 2
# Output: [4, 5, 1, 2, 3]

arr=[1, 2, 3, 4, 5]
k=int(input("enter a nummber : "))
k = k % len(arr)
for i in range(k):
    last=arr[-1]
    for j in range(len(arr)-2,-1,-1):
        # print(arr[j])
        arr[j+1]=arr[j]
    arr[0]=last
print(*arr)