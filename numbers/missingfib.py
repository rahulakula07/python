# sum of missing number in fibinoci series
num=int(input())
a,b,count,totalSum=0,1,0,0
while count!=num:
    for i in range(a+1,b):
        totalSum+=i
        count+=1
        print(i,end=" ")
        if count==num:
            break
    a,b=b,a+b
print(totalSum)