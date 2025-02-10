# Problem Statement: Given an array of N integers, the task is to replace each element of the array by its rank in the array.
num =[int(i) for i in input("enter:").split()]
num.sort()
print("sorted array :",num)
incArray =[]
decArray =[]
res =" "
for i in range(0,len(num)//2):
    incArray.append(num[i])

for i in range(len(num)//2,len(num)):
    decArray.append(num[i])

temp=decArray
temp.reverse()
finalArray=incArray+decArray
print("finalArray is",finalArray)
for i in finalArray:
    str_i=str(i)
    res+=str_i+" "
print(res)
#############################################################################################################################################



