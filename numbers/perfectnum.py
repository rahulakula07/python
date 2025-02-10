# wap to find a perfect number
num=int(input("enter a num:"))
res=0
for i in range(1,(num//2)+1):
    if(num%2==0):
        res+=i
if(res==num):
    print(f"{num} it is perfect num")
else:
    print(f"{num} it is not a perfect number")
#################################################################################################################
# wap to find perfect num upto given number
n=int(input())
c=0
for j in range(1,n+1):
    res=0
    for i in range (1,(j//2)+1):
        if j%i==0:
            res+=i
    if(j==res):
        print(j)
        c+=1
print(c)
####################################################################################################################