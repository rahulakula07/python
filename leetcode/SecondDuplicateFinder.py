# Write a program that takes array of numbers are input, print the second duplicate number and it’s occurrence.

# Testcase1	:  [ 64, 1, 2, 7, 79, 7, 7, 1, 22]
# Output     	:  Second duplicate number is 7 and it is occurred 3 times
# Explanation	: In the given array [ 64, 1, 2, 7, 79, 7, 7, 1, 22], the second duplicate number is 7 and it is occurred for 3 times.

# Testcase1	:  [ 121, 8, 1, 4, 5, 4, 8, 1 ]
# Output     	:  Second duplicate number is 1 and it is occurred 2 times
# Explanation	: In the given array [ 121, 8, 1, 4, 5, 4, 8, 1 ] the second duplicate number is 1 and it is occurred for 2 times.

arr=[ 121, 8, 1, 4, 5, 4, 8, 1 ]
res=[]
dup=[]
c=0
for i in arr:
    if i not in res:
        res+=[i]
    else:
        dup+=[i]
# print(dup)
seconddup=dup[1]
c=0
for i in arr:
    if i == seconddup:
        c+=1
print(c)

##############################################################
arr=[ 121, 8, 1, 4, 5, 4, 8 ]
res=[]
dup=[]
c=0
for i in arr:
    if i not in res:
        res+=[i]
    else:
        dup+=[i]
# print(dup)
seconddup=dup[1]
c=0
for i in arr:
    if i == seconddup:
        c+=1
if c>0:
    print("the second duplicate number is" ,seconddup, "and it is occurred for" ,c ,"times."
)
else:
    print("there is no second dupicate is present")