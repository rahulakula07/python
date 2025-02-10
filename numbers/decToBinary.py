# WAP to convert dec to binary

num = int(input("enter a num: "))
temp = num
binary =""

while num>=1:
    if num%2 == 0:
        binary += "0"
        num = num//2
    elif num%2 ==1:
        binary += "1"
        num = num//2
        
print("{} converted to binary is {}".format(temp,binary))