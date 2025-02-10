string=input() #abcdcdc
substring=input() #cdc
c=0
for i in range(0,len(string)):
    if string[i]==substring[0]:
        if(string[i:i+len(substring)]==substring):
            c+=1
print(c)

str1=input()
substr=int()
for i in range(0,len(str1)):
    if(str1[i]==substr[0]):
        if