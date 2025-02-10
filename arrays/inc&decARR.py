# rearrange the array such that the first half is arranged in incerse order and second half is arranged is arranged in decresing order 

# input: 8 7 1 6 5 9

# output : 1 5 6 9 8 7

# num = [int(i) for i in input("enter: ").split()]
# num.sort()
# print("sorted array is : ",num)
# incArr = []
# decArr = []
# res =" "

# for i in range(0,len(num)//2):
#     incArr.append(num[i])

# for i in range(len(num)//2,len(num)):
#     decArr.append(num[i])

# temp = decArr
# temp.reverse()
# finalArray = incArr + decArr
# print("finalarray  is : ",finalArray)
# for i in finalArray:
#     str_i = str(i)
#     res += str_i+" "
# print(res)

####################################################################################################################

# other method (sir told)

num = [int(i) for i in input().split()]
num.sort()
mid = len(num)//2
first = num[0:mid]
second = num[mid:]
second.sort(reverse=True)
print(* first+second)