arr=[int(i) for i in input("enter a nummber:").split()]
for i in num:
    if  not in uni:
f=arr[0]
l=arr[-1]
res=[]
for i in range(f,l+1):
    if i not in arr:
        res+=[i]
print(res)

num=arr=[int(i) for i in input("enter a nummber:").split()]
unq=[]
dup=[]
for i in num:
    if i not in unq and arr.count(i)==1:
        unq+=[i]
    elif i not in dup and arr.count(i)>1:
        dup+=[i]
print(unq)
print(dup)

str1=input("Enter:")
rev=""
for char in str1:
    # rev=char+rev
    rev+=char
    # print(rev)
print(rev)
if rev==str1:
    print("true")
else:
    print("not a palindrome")
##############################################################################

str1=input("enter:")
rev=""
for char in range(len(str1),0,-1):
    rev+=str(str1[char-1])
    # print(rev)
print(rev)

arr=[int(i) for i in input("enter a nummber:").split()]
k=int(input("enter :"))
for i in range(k):
    last=arr[-1]
    for j in range(len(arr)-1,0,-1):
        arr[j]=arr[j-1]
    arr[0]=last
print(*arr)


arr=[int(i) for i in input("enter").split()]
k=int(input("enter"))
# for i in range(k): #left
#     last=arr[-1]
#     # print(last)
#     for j in range(len(arr)-1,0,-1):
#         arr[j]=arr[j-1]
#     arr[0]=last
for i in range(k): #right 
    last=arr[0]
    # print(last)
    for j in range(len(arr)-1):
        # print(j)
        arr[j]=arr[j+1]
    arr[-1]=last
# print(*arr)
rotate=arr[-k:]+arr[:-k] #rotates the elments to the left
print(*rotate)
rotate=arr[k:]+arr[:k] #rotates the elements to right 
print(*rotate)
# enter1 2 3 4 5
# enter2
# 4 5 1 2 3
# [3, 4, 5, 1, 2]
#####################################################################

arr1=[int(i) for i in input("Enter:").split(",")] #[1,2,3,-1,-1,-2,-2]
res=[]
first,second=float("inf"),float("inf")
for n in arr1:
    if n<first:
        second,first=first,n  
    elif n>first and n<second:
        second=n
for n in arr1:
    if n==second:
        res+=[n]
print(res)
# output
# Enter:1,2,3,-1,-1,-2,-2
# [-1, -1]

arr1=[int(i) for i in input("Enter:").split(",")]
res=[]
first,second=float("inf"),float("inf")
for i in arr1:
    if i<first:
        second,first=first,i
    elif i>first and i<second:
        second=i
for i in arr1:
    if i==second:
        res+=[i]
print(res)


arr=[int(i) for i in input("enter: ").split()]
zero=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[zero],arr[i]=arr[i],arr[zero]
        zero+=1
print(arr)

arr=[int(i) for i in input("enter:").split()]
tar=int(input("enter tar"))
res=[]
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if arr[i]+arr[j]==tar:
            # res.append([arr[i],arr[j]])
            res+=[[arr[i],arr[j]]]
print(res)


arr=[int(i) for i in input("enter").split()]
res=[]
for i in range(1,len(arr)-1):
    if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
        res+=[arr[i]]
if arr[0]>arr[1]:
    res+=[arr[0]]
if arr[-1]>arr[-2]:
    res+=[arr[-1]]
print(res)
# enter2 1 29 1 2
# [2,29,2]

s=input("enter:")
res=""
for i in range(len(s)):
    if i==0 or i==len(s)-1:
        if "a"<= s[i]<="z":
            res+=chr(ord(s[i])-32)
        else:
            res+=chr(ord(s[i])+32)
    else:
        res+=s[i]
print(res)

# enter:Rahul
# rahuL

arr=input("enter").split()
res=[]
length=len(arr[0])
for i in range(1,len(arr)):
    if str(length)<str(len(arr[i])):
        length=len(arr[i])
for i in range(len(arr)):
    if str(length)==str(len(arr[i])):
        res+=[len(arr[i]),arr[i]]
print(res)
# entera ab abc abcd xyz pqrs
# [4, 'abcd', 4, 'pqrs']
# enterapple hello banana cherry
# [6, 'banana', 6, 'cherry']

s=input("enter:")
set={}
res=""
for i in s:
    if i not in set:
        set[i]=1
    else:
        set[i]+=1
for i in s:
    if set[i]==1:
        res+=i
print(res)
# enter:swiss
# wi

str1=input("enter:")
str2=input("enter:")
if len(str1) != len(str2):
    print("false")
else:
    combined=str1+str2
    if str2 in combined:
        print("true")
    else:
        print("false")
# output
# enter:abcde
# enter:cdeab
# true

s="aabccccaaa"
c=1
res=""
for i in range(1,len(s)):
    # c=1
    if s[i]==s[i-1]:
        c+=1
    else:
        res+=s[i-1]+str(c)
        c=1
res+=s[-1]+str(c)
print(res)
# a2b1c4a3

    
def is_anagram(s1,s2):
    fre_dict={}
    for i in s1: #s swiss
        if i in fre_dict:  
            fre_dict[i]+=1     
        else:
            fre_dict[i]=1
    count=0
    for i in s2:
        if i in fre_dict:
            fre_dict[i]-=1
            if fre_dict[i]==0:
                count+=1
            else:
                return False
    return count==len(fre_dict)
print(is_anagram("silent","listen"))  
# true

arr1=-10 
arr2=[]
for i in arr1:
    if isinstance(i,list):
        arr2.extend(i)
    else:
        arr2+=[i]
print(arr2)

# [1, 2, 3, 4, 5, 6, 7]





arr=[]
res=[]
a='abcd'
for ch in a:
    new_word=ch #b 
    for i in range(len(a)-1,-1,-1):
        if(ch!=a[i]):
            new_word+=a[i]
    arr+=[new_word]
res+=arr
for word in arr:
    new_word1=word[0]
    temp=word[0]
    for j in range(3,-1,-1):
        if(temp!=word[j]):
            new_word1+=word[j]
    res+=[new_word1]
print(res)

# output

# ['adcb', 'bdca', 'cdba', 'dcba', 'abcd', 'bacd', 'cabd', 'dabc']

# 5.Find All Permutations of a String
#       "abc" → ["abc", "acb", "bac", "bca", "cab", "cba"]
# Write a function to find all permutations of a given string.
# status: not solved missed logic

s=input("enter: ")
res=[]
for i in range(len(s)):
    for j in range(len(s)):
        if i==j:
            continue
        for k in range(len(s)):
            if k==i or j==k:
                continue
            res+=[s[i]+s[j]+s[k]]
print(res)
# enter: abc
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# Find the Longest Increasing Subsequence
#        [10, 9, 2, 5, 3, 7, 101, 18] → 4
# Write a function to find the length of the longest increasing subsequence in an array.
 
# ee question eroju adigindu
arr=[10, 9, 2, 5, 3, 7, 101, 18]
max_count=0
for i in range(len(arr)):
    c=1
    current=arr[i]
    for j in range(i+1,len(arr)):
        if arr[j]>current:
            c+=1
            current=arr[j] 
    if c >max_count:
        max_count=c
print(max_count)
# op
# 4
# if it is greter than previos the increse count id it is smaller that previous then count shoulkd b stay like that 
# 10 -1
# 19<10 -1 2< 9 -?>1 5>2 ->2 3<5=> 2 7>3=> 3 101>7=>4
# op shoulde be 4

# selection sort
arr=[64,25,11,21,10]
for i in range(len(arr)):
    minidx=i
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)
# [10, 11, 21, 25, 64]