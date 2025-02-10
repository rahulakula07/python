# num = int(input("enter a number: "))

# a,b = 0,1
# i =1
# while i<=num:
#     print(a, end=" ")
#     a,b = b,a+b
#     i+=1


####################################################################################################################
# using for loop



# num1 = int(input("enter a num1: "))
# a,b = 0,1
# for i in range (1,num1+1):
#     print(a)
#     a,b = b,a+b




####################################################################################################################

# upto  kth term of fibonacci series 


# num = int(input("enter a number: "))

# a,b = 0,1

# while a<=num:
#     print(a)
#     a,b = b, a+b


####################################################################################################################

# Q) given a num as string , if indiv num is fibanicc sum otherwise leve and return fibSum 

# num = input("enter a num: ")
# fibSum = 0

# def is_fib(n):
#     a,b = 0,1
#     while True:
#         if n == a:
#             return True
#         if n < n:
#             return False
#         a,b = b,a+b



# for i in num:
#     if is_fib(int(i)) :
#         fibSum += int(i)

# print(fibSum)

####################################################################################################################
####################################################################################################################


# num = int(input("enter a num: "))
# a,b = 0,1


# while a <= num:
#     # print(a)
#     a,b = b,a+b
# left,right = b-a,a
# # print(left,right)
# res = left if num-left < right-num else right
    
# print(res)

      
      

####################################################################################################################


# WAP to print first n numbers missing fib numbers.

# num = int(input("e: "))

# a,b = 0,1
# count = 0
# while num != count:
#     for i in range(a+1,b):
#         print(i,end=" ")
#         count += 1
#         if count == num:
#             break
#     a,b = b ,a+b


####################################################################################################################


# WAP to print the sum of nonfib numbers as per input

num = int(input("enter a number: "))
nonFibSum = 0
a,b = 0,1  # 1 1 # 1 2 # 2 3 # 3 5 # 5 8
count = 0
while num != count:
    for i in range(a+1,b):
        nonFibSum += i
        count += 1
        if count == num:
            break
    a,b = b ,a+b
    
print("the sum of missing non fib numbers is {}".format(nonFibSum))