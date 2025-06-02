# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# +1
# ++12
# +++123
# ++++1234


rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    print("+"*i,end="")
    for j in range(1,i+1):
        print(j,end="")
    print()