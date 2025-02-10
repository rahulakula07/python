
num = input("enter: ").split() # 10 20 30 10 40 50 20
# print(num)

l1=[]
uni,dup = "",""
for i in num:
    if i not in l1:
        l1.append(i)
for j in l1:
    if num.count(j) == 1:
        uni += j+" "
    else :
        dup += j+" "
        
print("uniq",uni)
print("dup",dup)
