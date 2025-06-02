# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# A 
# AB
# ABC
# ABCD


rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

