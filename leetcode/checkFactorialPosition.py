# Write a program that takes array of numbers as input and a number as second input. Check the position of the factorial of the second input number in the given array. Print the position of it. If the factorial of given second input number is not presented in the array then print factorial of  the number is not presented.

# Testcase1	:  [ 61, 4, 6, 7, 120 , 10 ]
# Input :  5
# Output     	: 4
# Explanation : In the given array of numbers[ 61, 4, 6, 7, 120 , 10 ], the factorial of second input number 5 is 120, it is presented at 4th position. So output is 5.

# Testcase1	:  [ 61, 4, 6, 7, 120 , 10 ]
# Input 2:  7
# Output     	: Factorial of 7 is not presented.
# Explanation	: Factorial of the second input number 7 is not presented in the given array of numbers.

arr=[ 61, 4, 6, 7, 120 , 10 ]
ip=int(input("enter number: "))
def factorial(s):
    res=1
    for i in range(1,s+1):
        res*=i
    return res
ip=factorial(ip)
for i in range(len(arr)):
    if arr[i] == ip:
        print(i)