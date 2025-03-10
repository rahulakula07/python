# 1) Program to print the primes in the range(1,50)
# 2) Program to print the sum of all primes numbers in the range(1,50).
# 3) Program to print the sum of all prime numbers that ends with 7 in the range(1,50).
# 4) Program to print the reverse of all the  numbers in the range(1,50).
# 5) Program to print the sum of individual digits in a number in the range(1,50)
# 6) Program to check whether the sum of individual digits is a prime number or not in the range(1,50)


# ques1 qand 2
sum=0
for i in range (1,51):
    if i<2:
        continue
    count=1
    for j in range(2,(i//2)+1):
        if i%j ==0:
            count=0
            break
    if count==1 :
        print(i)
        sum+=i
print(sum)

# output 328

# ----------------------------------------------
# ques3

sum=0
for i in range (1,51):
    if i<2:
        continue
    count=1
    for j in range(2,(i//2)+1):
        if i%j ==0:
            count=0
            break
    if count==1 and i%10==7 :
        print(i)
        sum+=i
print(sum)
# output
# 7
# 17
# 37
# 47
# 108
# ---------------------------------------------------------
# ques5


for i in range(1,51):
    sumdigit=0
    temp=i
    while temp >0:
        # digit=temp %10
        # sumdigit+=digit
        sumdigit+=temp%10 #combination of above to lines
        temp//=10
    print(sumdigit)
# output
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 10 2 3 4 5 6 7 8 9 10 11 3 4 5 6 7 8 9 10 11 12 4 5 6 7 8 9 10 11 12 13 5 

# to find the sum of  those numbers
sum=0
for i in range(1,51):
    sumdigit=0
    temp=i
    while temp >0:
        # digit=temp %10
        # sumdigit+=digit
        sumdigit+=temp%10 #combination of above to lines
        temp//=10
        sum+=sumdigit
    print(sumdigit,end=" ")
print(sum)
# output
# 510
# --------------------------------------------------------------------------------------------
# ques 6
for i in range(1,51):
    sumdigit=0
    temp=i
    while temp >0:
        # digit=temp %10
        # sumdigit+=digit
        sumdigit+=temp%10 #combination of above to lines
        temp//=10
    if sumdigit<2:
        isprime=False
    else:
        isprime=True
        for j in range(2,(sumdigit//2)+1):
            if sumdigit%j==0:
                isprime=False
                break
    print(isprime,end=" ")
    print(sumdigit,end=" ")
    # output
    # False 1 True 2 True 3 False 4 True 5 False 6 True 7 False 8 False 9 False 1 True 2 True 3 False 4 True 5 False 6 True 7 False 8 False 9 False 10 True 2 True 3 False 4 True 5 False 6 True 7 False 8 False 9 False 10 True 11 True 3 False 4 True 5 False 6 True 7 False 8 False 9 False 10 True 11 False 12 False 4 True 5 False 6 True 7 False 8 False 9 False 10 True 11 False 12 True 13 True 5 