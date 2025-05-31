# Write a program that takes a string, string should be of even length. Divide the string into two equals parts, check the number of vowels in both the parts of the string. If both parts of string have same number of vowels then return true otherwise return false.

# Testcase1	:  rebels
# Output     	:  true
# Explanation 	:  Given sring rebels divided into two parts, reb and els. In both parts vowels count is same that is 1(e is presented in both the parts) so it returns true.

# Testcase2	:  apples
# Output     	:  true

# Testcase1	:  mars
# Output     	:  false

s="rebels"
# res=[]
# for i in s:
#     res+=[i]
# print(res)
mid=len(s)//2
vowels = 'aeiouAEIOU'
first=s[:mid]
second=s[mid:]
# print(first,second)

def count(f):
    c=0
    for i in f:
        # print(i)
        if i in vowels:
            c+=1
    return c
# count(first,second)
countf=count(first)
counts=count(second)
# print(countf,counts)

if countf==counts:
    print("true")
else:
    print("false")

###########################################################################
def vowels(s):
    count=False
    res=[]
    for i in s:
        res+=[i]
    a=res[:len(res)//2]
    b=res[len(res)//2:]
    print(a,b)
    vowels="a,e,i,o,u"
    for i in vowels:
        if i in a or i in b:
            count=True
    return count        
s1="rebels"    
print(vowels(s1))
