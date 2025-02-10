num = [int(i) for i in input().split()]
temp = num.copy()
temp.sort()
res = ""
for i in range(len(num)):
    for j in range(len(temp)):
        if num[i] == temp[j]:
            res += str(j+1) + " "
            break
print(res)