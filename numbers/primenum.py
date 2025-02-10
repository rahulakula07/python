# find the maxprime in the given number

num=input("enter a number:")
res=" "
first=1
def isprime(n):
    if(n>1):
        for i in range (2,(n//2)+1):
            if n%i==0:
                return False
        return True
    return False
for digits in num:
    if(isprime(int(digits))):
        if(first==1):
            maxprime=digits
            first+=1
        else:
            if digits>maxprime:
                maxprime=digits
        
print(maxprime)
#############################################################################################################################

# find the left and right prime and print the nearest

num=int(input("ente a number:"))
def isprime(n):
    if(n>1):
        for i in range(2,(n//2)+1):
            if(n%i==0):
                return False
        return True
    return False
if(isprime(num)):
    print("it is a prime number")
else:
    leftprime,rightprime=num-1,num+1
    while True:
        if(isprime(leftprime)):
            print(leftprime)
            break
        leftprime-=1
    while True:
        if(isprime(rightprime)):
            print(rightprime)
            break
        rightprime+=1
    res= "{} {}".format (leftprime,rightprime) if(num-leftprime==rightprime-num)else leftprime if(num-leftprime<rightprime-num) else rightprime

################################################################################################################################
# wap to print the sum of max and min prime number

num=input("ente a number:")
maxprime=0
minprime=10
def isprime(n):
    if(n>1):
        for i in range(2,(n//2)+1):
            if(n%i==0):
                return False
        return True
    return False
for j in num:
    digit=int(j)
    if(isprime(digit)):
        if digit>maxprime:
            maxprime=digit
        if digit<minprime:
            minprime=digit
if maxprime!=0 and minprime!=10:
    primesum=maxprime+minprime
    print("sum of min and max prime is",primesum)
else:
    print("noprime number is found")
        