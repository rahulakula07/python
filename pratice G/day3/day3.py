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
0# 3

def missing(arr):
    n=len(arr)+1
    expectedsum=n*(n+1)//2
    originalsum=sum(arr)
    missing=expectedsum-originalsum
    return(missing)

arr=[int(i) for i in input("enter arr: ").split()]
print(missing(arr))

# output
# enter arr1: 1 2 4 5
# 3
###########################################
# to find all missing numbers\

arr = [int(i) for i in input("enter: ").split()]

res = []

for i in range(len(arr)-1):
    if(arr[i]+1 != arr[i+1]):
        res += [arr[i]+1]
        
print(res)
# output
# enter: 1 3 5 7 9 1
# [2, 4, 6, 8, 10]
##############################################
arr = [int(i) for i in input("enter: ").split()] # 1 2 4 5

first = arr[0]
last = arr[-1]
res = []

for i in range(first,last+1):
    if i not in arr:
        res += [i]
        
print(res)

# output
# enter: 1 3 5 7 9 1
# [2, 4, 6, 8, 10]
##########################
def missing(arr):
    arr=sorted(arr)  # Sort the array to ensure numbers are in order
    n=arr[-1] # Get the last number as the maximum expected value
    fullset=set(range(arr[0],n+1)) # Create a set from min to max number
    missing=list(fullset - set(arr))
    return(missing)

arr=[int(i) for i in input("enter arr: ").split()]
print(missing(arr))

# output:
# enter arr: 1 2 5 6 8 9
# [3, 4, 7]



# starpattens with numbers

rows = int(input("enter rows"))
val=1
for i in range(1,rows+1):
    for j in range (1,i+1):
        print(val,end=" ")
        val+=1
    print()

# output
# enter rows5
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

# question 2

rows = int(input("enter rows: "))
# val=1
for i in range(1,rows+1):
    val = i
    for j in range (1,i+1):
        print(val,end=" ")
        val+=1
    print()

# output
# enter rows: 5
# 1 
# 2 3 
# 3 4 5 
# 4 5 6 7 
# 5 6 7 8 9 

# question 3
rows = int(input("enter rows: "))
# val=1
for i in range(1,rows+1):
    val = i
    for j in range (1,i+1):
        print(val,end=" ")
        val+= rows-j
    print()

# output
# enter rows: 5
# 1 
# 2 6 
# 3 7 10 
# 4 8 11 13 
# 5 9 12 14 15

# question4
rows = int(input("enter rows: "))
# val=1
for i in range(1,rows+1):
    val = i
    for j in range (1,i+1):
        print(val,end=" ")
        val=val+rows-j
    print()

# output
# enter rows: 5
# 1 
# 2 6 
# 3 7 10 
# 4 8 11 13 
# 5 9 12 14 15 

# printng prime numbers in start patterns
rows = int(input("enter rows: "))
ele=(rows*(rows+1))//2
# val=1
arr=[]
def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    return False
i=1
while len(arr)<ele:
    if prime(i):
        arr.append(i)
    i+=1
print(arr)

for i in range(1,rows+1):
    val=i-1
    for j in range (1,i+1):
        print(arr[val],end=" ")
        val+=rows-j
    print()

# output
# enter rows: 5
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# 2 
# 3 13 
# 5 17 29 
# 7 19 31 41 
# 11 23 37 43 47 

# another pattern
rows = int(input("enter rows: "))
ele=(rows*(rows+1))//2
# val=1
arr=[]
def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    return False
i=1
while len(arr)<ele:
    if prime(i):
        arr.append(i)
    i+=1
print(arr)
val=0
for i in range(1,rows+1):
    # val=1
    for j in range (1,i+1):
        print(arr[val],end=" ")
        val+= 1
    print()

# enter rows: 5
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# 2 
# 3 5 
# 7 11 13 
# 17 19 23 29 
# 31 37 41 43 47 
# dimond patten

rows = int(input("enter: "))

for i in range(1,2*rows):
    stars = i if i<=rows else 2*rows-i
    spaces = rows-i if i<=rows else i-rows
    print(" "*spaces,end="")
    print("* "*stars)

# output
# enter: 5
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# hallo dimaond
rows = int(input("enter: "))

for i in range(1,2*rows):
    # stars = i if i<=rows else 2*rows-i
    spaces = rows-i if i<=rows else i-rows
    print(" "*spaces,end="")
    for j in range(1,rows+1):
        if j==1 or i==j or i+j==2*rows:
            print("* ",end="")
        else:
            print("  ",end='')
        # print("* ",end="")
    print()

# output
# enter: 5
#     *         
#    * *       
#   *   *     
#  *     *   
# *       * 
#  *     *   
#   *   *     
#    * *       
#     *  
