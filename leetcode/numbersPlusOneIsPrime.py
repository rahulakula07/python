# Write a program that takes array of numbers as input, among the numbers in array, print the numbers which forms a prime number by adding one to it. Print such numbers in the given array separated b spaces.

# Testcase1	:  [ 7, 4, 7, 23, 10 ]
# Output     	:  4 10
# Explanation : In the given array of number [ 7, 4, 7, 23, 10 ] the numbers 4 and 10 by adding one to these numbers, they formed prime number 5 and 11. So the output is 4 10.

arr= [ 61, 4, 6, 7, 120 , 10] 
res=[]
def prime(s):
    if s < 2:
        return False
    
    for i in range(2,int(s//2)+1):
        if s % i ==0:
            return False
    return True
for i in arr:
    # print(i+1)
    if prime(i+1):
        res+=[i]
print(res)