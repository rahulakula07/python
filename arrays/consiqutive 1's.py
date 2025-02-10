# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# def findMaxConsecutiveOnes(num):
#     m=c=0
#     for i in num:
#         if i == 1:
#             c += 1
#         else:
#             c=0
#         m = max(m,c)
#     return m

# num = [int(i) for i in input().split()]
# res = findMaxConsecutiveOnes(num)
# print(res)


######################################## OTHER METHOD ##############################################################

#  with out using functions

num = input().split()
c=max1=0
for i in num:
    if i=="1":
        c+=1
    else:
        c=0
    max1 = max(max1,c)
print(max1)