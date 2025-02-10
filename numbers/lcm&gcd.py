#####################  LCM ######################

a = int(input("enter a num: "))
b = int(input("enter a num: "))

max1 = a if a>b else b
temp = max1

while True:
    if max1%a==0 and max1%b==0:
        print("LCM is : " ,max1)
        break
    else:
        max1 += temp
        
gcd = (a*b)//max1
print("GCD is : ",gcd)


#####################  GCD ######################

a = int(input("enter a num: "))
b = int(input("enter a num: "))

for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        gcd = i
        break
print("gcd is : ", gcd)

print("LCM is : ", (a*b)//gcd)