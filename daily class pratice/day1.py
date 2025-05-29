# print uni numbers
arr=[int(i) for i in input().split()]
res=[]
def count(k):
    co=0
    for j in arr:
        if k==j:
            co+=1
    return(co)
    
for i in arr:
    if i not in res and arr.count(i)==1:
        res+=[i]
print(res)
# output
# 1 2 2 3 3 4 5 5
# [1, 4]
#####################################################################
arr=[int(i) for i in input().split()]
res=[]
for i in arr:
    if i not in res and arr.count(i)==1:
        res+=[i]
print(res)
# output
# 1 2 2 3 3 4 5 5
# [1, 4]
######################################################################

# Enter:apple,banana,cherry,grapes
# ['apple', 'banana', 'cherry', 'grapes']
# banana
# 6
arr1=input("Enter:").split(",")
print(arr1)
maxi=len(arr1[0])
for i in range(1,len(arr1)):
    if len(arr1[i])>maxi:
        print(arr1[i])
        maxi=len(arr1[i])
print(maxi)            


arr=input("enter: ").split(",")
max_len=len(arr[0])
for i in arr:
    if len(i)>max_len:
        max_len=len(i)
print(max_len)
        
# Enter:apple,banana,cherry,grapes
# ['apple', 'banana', 'cherry', 'grapes']
# banana
# 6
arr=input("enter:").split(",")
print(arr)
max_len=0
dic=""
for i in arr:
    if len(i) >max_len:
        dic=len(i)
print(dic)

# Enter:apple,banana,cherry,grapes
# ['apple', 'banana', 'cherry', 'grapes']
# banana
# 6

#####################################################################################################
arr=input("enter:").split(",")
# print(arr)
num_len=[]
dic=[]
for i in arr:
    if len(i) >0:
        num_len+=str((i)).split(",")
print(num_len)
max_len=num_len[0]
for j in range(1,len(num_len)):
    if num_len[j] >str(max_len) or num_len[j]==max_len:
        max_len=num_len[j]
        dic+=max_len.split(",")
print(dic)


# output
# enter:apple,banana,cherry,grapes
# ['apple', 'banana', 'cherry', 'grapes']
# ['banana', 'cherry', 'grapes']
arr=input("enter:").split(",")
num_len=[]
dic=[]
for i in arr:
    if len(i) >0:
        num_len+=str(len(i))
print(num_len)
max_len=num_len[0]
for j in range(1,len(num_len)):
    if num_len[j] >str(max_len) or num_len[j]==max_len: 
        max_len=num_len[j] 
        dic+=max_len 
print(dic)

# enter:apple,banana,cherry,grapes
# ['5', '6', '6', '6']
# ['6', '6', '6']
# #################################################################################


arr=[[1, [2, 3]], [4, [5, 6]], 7]
arr1=[]
for i in arr:
    if isinstance(i,list):
        for j in i:
            if isinstance(j,list):
                for k in j:
                    arr1+=[k]
            else:
                arr1+=[j]
    else:
        arr1+=[i]
print(arr1)
# op
# [1, 2, 3, 4, 5, 6, 7]


            

