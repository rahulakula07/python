# Question 
# 1) given arr, we need to find uni and dup in sorted order

# num = input().split()
# num.sort()
# uni=dup=" "
# temp = []
# for i in num:
#     if i not in temp:
#         temp.append(i)

# for i in temp:
#     if num.count(i) >1:
#         dup += i + " "
#     else:
#         uni += i + " "
# print("uni : ", uni)
# print("dup : ",dup)


####################################################################################################################

#method-2

# num = [int(i) for i in input().split()]
# num.sort()

# uni=dup=" "
# temp = []
# for i in num:
#     if i not in temp:
#         temp.append(i)

# for i in temp:
#     if num.count(i) > 1:
#         dup += str(i) + " "
#     else:
#         uni += str(i) + " "

# print("uni",uni)
# print("dup",dup)


#######################################  NEW QUESTION ##############################################################

# remove duplicaties and return length of new array

num  = input().split()
temp = []
for i in num:
    if i not in temp:
        temp.append(i)
print(len(temp))