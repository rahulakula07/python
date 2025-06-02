# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 3
# Output     	: 

#    A
#  A  B
# A  B  C

rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    print(" "*(rows-i),end="   ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

