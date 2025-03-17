# 1) Program to print the sum of all prime digits in a number
# input: 46732
# output: 12
# 2) Program to print the prime digits in a number in asc order
# output: 237
# 3) Prgroam to print the pirme digits in desc order in a number.
# output: 732

# 4) Program to find the largest digit in the given number
# input: 1754
# output : 7


num=input("Enter:")   #46732
primdigits=[]
for i in num:
    # x=int(i)
    div=0
    for j in range(2,(int(i)//2)+1):
        if int(i)%j==0:
            div+=1
            break
    if div==0:
        primdigits+=i
        primdigits.sort()
# sorted_primdigits = "".join(sorted(primdigits)) 
des=primdigits[::-1]
print(des[0])

# output
# Enter:46732
# 7
# --------------------------------------------------------------------------------------------------
# with methods
num=input()
dec=sorted(num)[::-1]
print(dec[0])

# output
# 1245789
# 9

# without methods
num=input()
max1=num[0]
for i in range(1,len(num)):
    if num[i]>max1[0]:
        max1=num[i]
print(max1)   
# output   
# 12457
# 7 
# -----------------------------------------------------------------------------------------------------
num=[int(i) for i in input().split(",")]
print(num)
max1=num[0]
for i in range(1,len(num)):
    if num[i]>max1:
        max1=num[i]
print(max1)     

