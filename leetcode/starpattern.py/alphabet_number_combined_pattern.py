# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# A1
# AB12
# ABC123
# ABCD1234

rows=int(input("enter no of rows :  "))
for i in range(1,rows+1):
    for j in range(i):
        print(chr(65+j),end="")
    for k in range(1,i+1):
        print(k,end="")
    print()