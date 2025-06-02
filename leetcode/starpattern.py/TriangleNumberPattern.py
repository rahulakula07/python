# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# 1
# 1 2
# 1 2 3
# 1 2 3 4

rows=int(input("enter no of rows:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
