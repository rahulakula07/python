# to find the number in a given string is fibonace or not############################################################################
num=input("enter a number")
sumfib=0
def fib(n):
    a,b=0,1
    while True:
        if a==n:
            return  True
        if a>n:
            return False
        a,b=b,a+b
for i in num:
    if(fib(int(i))):
        sumfib+=int(i)
print(sumfib)
#############################################################################################

# find the left and right fibonace number for a given number 

num = int(input("enter a: "))
a,b = 0,1

while a <= num:
    # print(a)
    c = a+b
    a,b = b,c
left, right = b-a,a

print(left,right)


# minLeft = num-left
# minRight = right-num
res=left if num-left<right-num else right
print(res)
# #############################################################################################################



    