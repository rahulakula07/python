# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 3
# Output     	: 

#     1   
#   1   2   
# 1   2   3   

rows=int(input("enter no of rows:"))
for i in range(1,rows+1):
    print(" "*(rows-i)*2,end=" ")
    for j in range(1,i+1):
        print(j,end="   ")
    print()
