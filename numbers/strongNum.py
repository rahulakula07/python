num = input("enter a number: ") #145
result = 0
for char in num:
    i = int(char)
    fact = 1
    for j in range(1,i+1):
        fact *= j
    result += fact
if int(num)==result:
    print("strong number")
else :
    print("not a strong number")

####################################################################################################################