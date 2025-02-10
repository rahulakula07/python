# 1) WAP to print the nearest prime to the given number
# input: Enter number: 18
# output: 17 19
# input: Enter number: 25
# output: 23

# num = int(input("enter a num : "))

# def isPrime(n):
#     if n>1:
#         for i in range(2,(n//2)+1):
#             if n%i ==0:
#                 return False
#         return True
#     return False
    
# if isPrime(num):
#     print("it is prime")
# else:
#     lp,rp = num-1, num+1
#     leftPrime,rightPrime = None, None
    
#     while not (leftPrime and rightPrime):
#         if not leftPrime and isPrime(lp):
#             leftPrime = lp
#         if not rightPrime and isPrime(rp):
#             rightPrime = rp
#         lp -= 1
#         rp += 1

#     print("left prime is",leftPrime,"and Right prime is",rightPrime)
#     res = "{},{}".format(leftPrime,rightPrime) if num-leftPrime == rightPrime-num else leftPrime if num-leftPrime < rightPrime-num else rightPrime

#     print(res)
####################################################################################################################

# 2) WAP to print the sum of max and min prime in a given number
# input: Enter number: 1875
# output: 12

# num = input("enter a num: ")

# def isPrime(n):
#     if n>1:
#         for i in range(2,(n//2)+1):
#             if n%i == 0:
#                 return False
#         return True
#     return False
 

# maxPrime,minPrime = None,None   
# for i in num:
#     i = int(i)
#     if isPrime(i):
#         if maxPrime == None or i > maxPrime:
#             maxPrime = i
#         if minPrime == None or i < minPrime:
#             minPrime = i

# if maxPrime == None and minPrime == None:
#     print("no prime numbers")
# else :
#     print("sum of maxPrime({}) and minPrime({}) is {}".format(maxPrime,minPrime,maxPrime+minPrime))
            
        
        