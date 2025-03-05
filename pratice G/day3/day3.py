# Intersection of Two Arrays
#       [1, 2, 3], [2, 3, 4]  → [2,3]
# Write a function that returns the common elements between two arrays.
# 

arr1=input("a1").split()
arr2=input("a2").split()
result=[]
for num in arr1:
    if num in arr2:
        result.append(num)
print(result)

# output
# a1 1 2 3 4
# a2 1 2 4 5 6
# ['1', '2', '4']

#  in functions

def inserction(arr1,arr2):
    result=[]
    for num in arr1:
        if num in arr2:
            result.append(num)
    return(result)
arr1=input("enter arr1: ").split()
arr2=input("enter arr2: ").split()
print(inserction(arr1,arr2))

# output
# enter arr1: 1 2 3 4
# enter arr2: 1 2 3 4 5 6 7
# ['1', '2', '3', '4']

def inserction(arr1,arr2):
    return list(set(arr1) & set(arr2))
arr1=input("enter arr1: ").split()
arr2=input("enter arr2: ").split()
print(inserction(arr1,arr2))

# output
# enter arr1: 1 2 3 4 5
# enter arr2: 1 2 6 7 8 9
# ['1', '2']


# Find Missing Number
#        [1, 2, 4, 5]   → [3]
# Given an array of consecutive numbers with one missing, find the missing number.

arr=[int(i) for i in input("enter arr1: ").split()]
# print(arr)
n=len(arr)+1 # The array should have n elements (including the missing one)
expectedsum=n*(n+1) // 2  # Sum of first n natural numbers
actualsum = sum(arr)
missing=expectedsum - actualsum
print(missing)

# output
# enter arr1: 1 2 4 5
# 3

