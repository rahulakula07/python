# Q)  

#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 


# rows = int(input("enter rows: "))

# for i in range(1,rows+1):
#     for s in range(rows-i):
#         print(" ",end="")
        
#     for j in range(i):
#         print(j+1,end=" ")
#     print()

#################################################################################################################

#  Q)

# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

# rows = int(input("enter rows: "))

# for i in range(1,rows+1):
#     val=1
#     for j in range(rows-i+1,0,-1):
#         print(val,end=" ")
#         val+= 1
#     print()

# other method
rows = int(input("Enter rows: "))
for i in range(rows,-1,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#################################################################################################################

# Q) 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

rows = int(input("enter rows: "))

for i in range(1,rows+1):
    for s in range(i-1):
        print(" ", end="")
    for j in range(rows-i+1,0,-1):
        print("*",end=" ")
    print()
        