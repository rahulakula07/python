# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# 4 3 2 1
# 4 3 2
# 4 3
# 4

rows=int(input("enter no of rows:"))
for i in range(rows):
    for j in range(rows,i,-1):#if i = 0 1st line if i = 1 then 2nd line
        print(j,end=" ")
    print()