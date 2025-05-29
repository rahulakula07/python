# Find the Maximum Product of Two Elements
#        [3, 5, -2, 8, 11] → 8*11 →88
# Write a function to find the maximum product of two elements in an array

# with usinng method 
arr=input().split(",")
arr.sort(reverse=True)
print(arr)
print(int(arr[0])*int(arr[1]))

arr=[int(i) for i in input().split(",")]
arr.sort()
print(arr)
print(arr[-1]*arr[-2])
# Output
# 1,2,3,4,5
# ['5', '4', '3', '2', '1']
# 20
# 1,2,3,4,5
# [1, 2, 3, 4, 5]
# 20

# without using methods
arr=[int(i) for i in input().split(",")]
max1,max2=float("-inf"),float("-inf")
for i in arr:
    if i>max1:
        max2,max1=max1,i
    elif i>max2:
        max2=i
print(max1*max2)
# OUTPUT
# 1,2,3,4,5
# 20
######################################################################

# Move Zeros to End
#        [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
# Write a function that moves all zeros in an array to the end while maintaining the order of other elements.


# withOut Using MEthpds
num=[int(i) for i in input().split()]
res=[]
for i in num:
    if i !=0:
        res.append(i)
res=res+[0]*(len(num)-len(res))
print(res)

# OUTPUT
# 1 2 3 0 4 0 5 0
# [1, 2, 3, 4, 5, 0, 0, 0]

arr=[int(i) for i in input().split()]
zero=0
for i in range (len(arr)):
    if arr[i]!=0:
        arr[zero],arr[i]=arr[i],arr[zero]
        zero+=1
print(arr)
# OUTPUT
# 1 2 45 0 12 0 45 0 55 0 
# [1, 2, 45, 12, 45, 55, 0, 0, 0, 0]
###################################################################################
# Pair Sum
#        [2, 4, 3, 5, 7, 8, 9], 7 →  [[4, 3], [2, 5]]
# Write a function to find all pairs in an array whose sum is equal to a given target.

num=input().split()
tar=int(input())
tarsum=[]
for i in range(0,len(num)):
    for j in range (i+1,len(num)):
        if int(num[i])+int(num[j])==tar:
            tarsum.append([num[i],num[j]])
print(tarsum)
# OUTPUT
# 1 2 4 5 3 7 6 1
# 5
# [['1', '4'], ['2', '3'], ['4', '1']]
num=input().split()
tar=int(input())
tarsum=[]
for i in range(0,len(num)):
    for j in range (0,len(num)):#(here by placing range 0 here dupicates also come here )
        if int(num[i])+int(num[j])==tar:
            tarsum.append([num[i],num[j]])
print(tarsum)
# OUTPUT
# 1 2 4 5 3 7 6 1
# 5
# [['1', '4'], ['2', '3'], ['4', '1'], ['4', '1'], ['3', '2'], ['1', '4']]
#########################################################################################
# SORTED arr
num=[int(i) for i in input().split()]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[j]<num[i]:
            num[i],num[j]=num[j],num[i]
print(num)
# OUTPUT
# 5 4 3 2 1
# [1, 2, 3, 4, 5]
############################################################################################
# Find Peak Element
#        [1, 3, 20, 4, 1, 0] →  20
# Write a function to find a peak element in an array. An element is a peak if it is not smaller than its neighbours.

arr=[int(i) for i in input().split()]
peak=arr[0]
for i in range(1,len(arr)):
    if arr[i]>peak:
        peak = arr[i]
print(peak)
# OUTPUT
# 100 2 0 40 3 050
# 100
#################################################################################################
# Find the First Duplicate
#        [2, 1, 3, 5, 3, 2] → 3
# Write a function to return the first duplicate value in an array.

arr=[int(i) for i in input().split()]
dup=set()
for i in arr:
    if i in dup:
        print(i)
# OUTPUT
# 1 2 3 4 2 3 5 6
# 2
# 3
arr=[int(i) for i in input().split()]
dup=set()
for i in arr:
    if i in dup:
        print(i)
    dup.add(i)   #here it print the duplicate. 
print(dup)#here it print the set{}
#  OUTPUT
# 1 2 3 1 2 3 4 
# 1
# 2
# 3
# {1, 2, 3, 4}
######################################################################################################

