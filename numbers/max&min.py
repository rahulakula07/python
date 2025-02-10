# WAP to find max, min, sum of max&min and print max if maximun numbers comes comes first and wise vers

num = input("enter a num: ")  #1234

high = num[0]
low = num[0]
highIndex,lowIndex = 0,0

for i in range(1,len(num)):
    if num[i] > high :
        high = num[i]
        highIndex = i
    if num[i] < low :
        low = num[i]
        lowIndex = i

print("the highiest digite in the given {} is : {} and the index value is {}.".format(num,high,highIndex))
print("the lowest digite in the given {} is : {} and the index value is {}.".format(num,low,lowIndex))
print("the sum of low and high value is {}+{}={}".format(low,high,(int(low)+int(high))))

if highIndex > lowIndex :
    print("min")
else:
    print("max")



####################################################################################################################

# WAP to print max even digite in a number

num = input("enter a num: ")

maxEven = -1
minEven = 8

for i in num:
    digt = int(i)
    if digt%2 == 0 :
        if digt > maxEven:
            maxEven = digt
        if digt < minEven:
            minEven = digt


if maxEven == -1 :
    print("there is no even numbers in given num")
else :
    print(maxEven)


####################################################################################################################
# same upper question but for max and min
num = input("enter a num: ")

maxEven = 0
minEven = int(num[0])
countEven = 0

for i in num:
    digt = int(i)
    if digt%2 == 0 :
        countEven += 1
        if digt > maxEven:
            maxEven = digt
        if digt < minEven:
            minEven = digt

if countEven != 0 :
    print("the MaxEven number of {} is : {}".format(num,maxEven))
else:
    print("there is no even numbers in {}".format(num))
    
if countEven != 0 :
    print("the MinEven number of {} is : {}".format(num,minEven))
else:
    print("there is no even numbers in {}".format(num))
    
####################################################################################################################