# num = list(input("enter : "))

# for i in range(0,len(num)):
#     if num[i] == "0":
#         num[i] = "1"
#     elif num[i] == "1":
#         num[i] = "0"


# print("".join(num))

############################################################################################################


num = input("enter: ")
res = ""
for i in num:
    if i == "0":
        res += "1"
    elif i =="1":
        res +="0"
    else:
        res += i
        
print(res)