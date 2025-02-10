# find the max number in the row
# input: [[1,2,3],[4,3,2],[10,5,4]]
# output: 
# row1 max: 3
# row2 max: 4
# row3 max: 10

row,col = [int(i) for i in input().split()]
mat = []
for i in range(row):
    ele = [int(i) for i in input().split()]
    mat.append(ele)
# print(mat)

for i in range(len(mat)):
    max1 = float('-inf')
    for j in range(len(mat[i])):
        if mat[i][j] > max1:
            max1 = mat[i][j]
    print(f"max in row {i+1} is : {max1}")
######################################################################################################
# find the max number in the row with functions

# input: [[1,2,3],[4,3,2],[10,5,4]]
# output: 
# row1 max: 3
# row2 max: 4
# row3 max: 10

row,col = [int(i) for i in input().split()]
mat = []
for i in range(row):
    ele = [int(i) for i in input().split()]
    mat.append(ele)
# print(mat)

for i in range(len(mat)):
    print(f"row{i+1} max: {max(mat[i])}")

########################################################################################################################
#  WAP to print matrix

# row,clo = [int(i) for i in input().split()]
# mat =[]
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# print(mat)

# for i in range(len(mat)):
#     res = ''
#     for j in range(len(mat[i])):
#         res += str(mat[i][j])+" "
#     print(res)


####################################################################################################################

# WAP to transpose the matrix

# row,clo = [int(i) for i in input().split()]
# mat =[]
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# print(mat)

# for i in range(len(mat)):
#     res = ''
#     for j in range(len(mat[i])):
#         res += str(mat[j][i])+" "
#     print(res)

####################################################################################################################
#  Q)  WAP to print sum of diagonals of matrix

# row,clo = [int(i) for i in input().split()]
# mat =[]
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# print(mat)

# res = 0
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         if i==j or (i+j)==row-1:
#             res += mat[i][j]
# print(res)


####################################################################################################################


# Q) WAP to print outer layer of a matrix

# row,clo = [int(i) for i in input().split()]
# mat =[]
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# print(mat)


# for i in range(len(mat)):
#     res = ''
#     for j in range(len(mat[i])):
#         if i==0 or j==0 or i==row-1 or j==clo-1:
#             res += str(mat[i][j])+" "
#         else:
#             res += "  "
#     print(res)
        
####################################################################################################################
# Q) WAP to print max number in each row of matrix

# input: [[1,2,3],[4,3,2],[10,5,4]]
# output: 
# row1 max: 3
# row2 max: 4
# row3 max: 10

# row,col = [int(i) for i in input().split()]
# mat = []
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# # print(mat)

# for i in range(len(mat)):
#     print(f"row{i+1} max: {max(mat[i])}")

####################################################################################################################

        
        