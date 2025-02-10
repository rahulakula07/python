str1 = input()    #abcdcdc
subStr = input()  # cdc
c=0
for i in range(0,len(str1)):
    if str1[i] == subStr[0]:
        if (str1[ i : i+len(subStr) ] == subStr):
            c+=1
print(c)