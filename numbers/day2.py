# to find the sum of min and max num in agiven string
num=input("enter a number: ")
max1=num[0]
min1=num[0]
for i in range(1,len(num)):
    if num[i]>max1:
        max1=num[i]
    if num[i]<min1:
        min1=num[i]
sum2=int(max1)+int(min1)
print("the sum of max and min in{} is :{}".format(num,sum2))
# # --------------------------------------------------------------------------------------
# to find the min or max num is first in the given string
num=input("enter a number: ")
max1=num[0]
min1=num[0]
minind,maxind=0,0
for i in range(1,len(num)):
    if num[i]>max1:
        max1=num[i]
        maxind=i
    if num[i]<min1:
        min1=num[i]
        minind=i
result="maximum" if maxind < minind else "minimum"
print(result)
# # ----------------------------------------------------------------------------------------
# TO print the max even number in the given string
num=input("enter a number:")
maxeven=0
for i in range (len(num)):
    x=int(num[i])
    if(x%2==0):
        if(x>maxeven):
            maxeven=x
print(maxeven)
# # --------------------------------------------------------------------------------------------
# to print the max and min even numbers  ina sting
num=input("enter a number:")
maxeven=0
mineven=10 #we can use none/folat('inf') instaed of 10
for i in range (len(num)):
    x=int(num[i])
    if(x%2==0):
        if(x>maxeven):
            maxeven=x
        if(x<mineven):
            mineven=x
if(maxeven==0):
    print("no even number is found")
else:
    print(maxeven)
    print(mineven)
# # --------------------------------------------------------------------------------------------
# TO print the max and min digit in a num using while loop
num=input("enter a number:")
max1=num[0]
min1=num[0]
i=1
while i<len(num):
    if num[i]>max1:
        max1=num[i]
    if num[i]<min1:
        min1=num[i]
    i+=1
sum1=int(max1)+int(min1)
print("the sum of max and min numbers {}is :{}".format(num,sum1))
# ------------------------------------------------------------------------------------------------
str1=input("enter a string:")
alpha,digits,splchar=0,0,0
i=0
while i < len(str1):
    if (str1[i]>='A' and str1[i]<='Z') or (str1[i]>='a' and str1[i]<='z'):
        alpha+=1
    elif(str1[i]>='0' and str1[i]<'9'):
        digits+=1
    else:
        splchar+=1
    i+=1
print("aphabets:",alpha)
print("digits:",digits)
print("splchar:",splchar)
if (alpha==digits==splchar):
    print("same number of charaters")
else:
    result="alphabets" if alpha>digits and alpha>splchar else "digits" if digits>splchar else  "special character"
    print(result)
# -------------------------------------------------------------------------------------
