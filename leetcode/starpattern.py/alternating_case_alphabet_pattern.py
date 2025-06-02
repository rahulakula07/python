# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# A
# ab
# ABC
# abcd
rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        if i%2 == 0:
            print(chr(96+j),end="")
        else:
            print(chr(64+j),end="")
    print()
################################################
rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    for j in range(i):
        if i%2 == 0:
            print(chr(97+j),end="")
        else:
            print(chr(65+j),end="")
    print()