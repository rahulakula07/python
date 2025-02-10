num = int(input("enter "))
comb = False

def prime(n):
    if n>1:
        for j in range(2,(n//2)+1):
            if n%j == 0:
                return False
        return True
        
    return False

for i in range(2,num):
    if prime(i) and prime(num-i):
        print(i,num-i)
        comb = True
        break
    
if(comb):
    print(comb)
else:
    print(comb)