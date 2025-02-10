num = int(input("enter a num : "))
temp = num
res  = 0
while num != 0:
    rem = num%10
    res = res*10 + rem
    num = num//10
if(res == temp):
    print("{} is palmdrom number".format(temp))
else:
    print("{} is not palimdrom number".format(temp))

###################################################################################################################

# palindrome numbers upto given number

num = int(input("enter a num : "))

for i in range(1,num+1):
    temp = i
    res  = 0
    while i != 0:
        rem = i%10
        res = res*10 + rem
        i = i//10
    if(temp == res):
        print(temp)


####################################################################################################################

# WAP to print first first n number prime and palindrome numbers

num = int(input("enter a num : "))

def isPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i == 0:
                return False
        return True
    return False
    
    
for i in range(1,num+1):
    if isPrime(i):
        temp = i
        res  = 0
        while i != 0:
            rem = i%10
            res = res*10 + rem
            i = i//10
        if(temp == res):
            print(temp)