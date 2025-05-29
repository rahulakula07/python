# Check if Array is Sorted
#       [1, 2, 3, 4, 5]  →  true
# Write a function to check if an array is sorted in ascending order.

numbers = [1, 2, 3, 4, 5]
for num in range(1,len(numbers)-1):## ✅ Loop from 0 to len(numbers) - 2
    if numbers[num] > numbers[num + 1]:
        print("not sorted")
        break
else:
    print("sorted")


num=input().split()
print(num)
for i in range(1,len(num)-1):
    if num[i]>num[i+1]:
        print("not sorted")
        break
else:
    print("sorted")

# op sorted

# with functions
numbers = [1, 2, 3, 4, 5]
sort=sorted(numbers)
print(sort)
if numbers==sort:
    print("sort")
else:
    print("not sort")

# op sort
###########################################################################################
# Reverse an Array
# [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]
# Write a function to reverse the elements in an array.

numbers=[1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

# output [5, 4, 3, 2, 1]

numbers=[1, 2, 3, 4, 5]
num=numbers[::-1]
print(num)

# output [5, 4, 3, 2, 1]
############################################################################################
# Find Unique Elements
#        [1, 2, 2, 3, 4, 4, 5] → [1, 3, 5]
# Write a function to find the unique elements in an array (elements that appear only once).

num=input().split()
num.sort()
print(num)
temp=[]
for i in num:
    if i not in temp:
        temp.append(i)
print(temp)
# op
# 1 2 3 4 5 6 1 2 3 4 5 6
# ['1', '2', '3', '4', '5', '6']

num = input().split()
num.sort()
uni=dup=" "
temp = []
for i in num:
    if i not in temp:
        temp.append(i)

for i in temp:
    if num.count(i) >1:
        dup += i + " "
    else:
        uni += i + " "
print("uni : ", uni)
print("dup : ",dup)

# 1 2 3 4 5 6 1 2 3 4 
# uni :   5 6 
# dup :   1 2 3 4 
######################################################################################################'

# Sum of Even Numbers
#        [1, 2, 3, 4, 5] →  6
# Write a function that returns the sum of all even numbers in an array.

num = input().split()
sum=0
for i in num:
    if int(i)%2==0:
        sum+= int(i)
print(sum)

# output
# 1 2 3 4 5 6 1 2 3 4
# 18

# prime and non prime sum
num = input().split()
sum=0
npsum=0
for i in num:
    if int(i)%2==0:
        sum+= int(i)
    else:
       npsum+= int(i) 
print(sum,npsum)
# output
# 1 2 3 4 5 6 1 2 3 4

# 18 13
##########################################################################################################

# Rotate an Array
#       [1, 2, 3, 4, 5], 2  → [4, 5, 1, 2, 3]
# Write a function that rotates an array to the right by a given number of steps.

num = input().split(",")
k = int(input())

for i in range(k):
    last = num[-1]  # Store last element
    for j in range(len(num) - 1, 0, -1):  # Shift elements right
        num[j] = num[j - 1]
    num[0] = last  # Place last element at the first position

print(*num)
 
# output
# 1,2,3,4,5
# 3
# 3 4 5 1 2

num=[1,2,3,4,5]
for i in range(len(num)-1,-1,-1):
    print(i)
#########
num=[1,2,3,4,5]
res=[]
for i in range(len(num)-1,-1,-1):
    res.append(num[i])
print(res)
# output
# [5, 4, 3, 2, 1]
# to reverse the arry we use this 

# using sclicing method
num=input().split(",")
print(num)
k=int(input())%len(num)
num=num[-k:]+num[:-k]
print(* num)
# output
# 1,2,3,4,5
# 3
# 3 4 5 1 2
##################################################################################################################
# amstrong number
num = input("enter: ")
length = len(num)
c_sum = 0
for i in num:
    num_i = int(i)
    c_sum += num_i**length
    
if(c_sum == int(num)):
    print("amstrong")
else:
    print("not")
# output
# 371
# amstrong
############################################################################################################
# Lowest two values from array
# [1,2,5,7,8,-1,-1]
# Convert Helloworld to given output
# HelloWOrld
#hello worlD

arr=input("enter:--").split()
low1=float("inf")
low2=float("inf")

for i in arr:
    if i < str(low1):
        low2=low1
        low1=i
    elif i < str(low2):
        low2=i
print(low1,low2)
# op
# enter:--1 2 3 4 5 -2 -1
# -1 -2