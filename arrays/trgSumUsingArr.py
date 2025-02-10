
def targetSum(num,tar):
    for i in range(0,len(num)):
        for j in range(0,len(num)):
            if int(num[i]) + int(num[j]) == 0:
                return "yes"
    return "no"

num = input().split()
tar = int(input())
print(targetSum(num,tar))
