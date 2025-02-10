str1 = input("enter a string: ")
alph,digit,sp = 0,0,0

for i in str1:
    if (i >= 'A' and i<='Z') or (i>= 'a' and i<= 'z'):
        alph += 1
    elif i>='0' and i<='9' :
        digit += 1
    else :
        sp += 1
        
print("Alphabets are: ",alph)
print("Digits are: ", digit)
print("Special characters are: " ,sp)


    
    
if alph == digit and digit == sp and sp == alph :
    print("all has same no of characters")
else:
    highCount = "Alphabets" if alph>digit and alph > sp else "Digits" if digit>sp else "Special characters"
    print("high count characters is: ", highCount)
    

####################################################################################################################

# WAP to check whether alphabets count is more or digits count is more or special characters count is more using while loop.

str1 = input("enter a string: ")
alph,digit,sp = 0,0,0

i = 0
while i<=len(str1)-1:
    if (str1[i]>='A' and str1[i]<='Z') or (str1[i]>='a' and str1[i]<='z'):
        alph += 1
    elif str1[i]>='0' and str1<='9':
        digit += 1
    else :
        sp += 1
    i+=1
print("Alphabets are: ",alph)
print("Digits are: ", digit)
print("Special characters are: " ,sp)

if alph == digit and digit == sp and sp == alph :
    print("all has same no of characters")
else:
    highCount = "Alphabets" if alph>digit and alph > sp else "Digits" if digit>sp else "Special characters"
    print("high count characters is: ", highCount)
    