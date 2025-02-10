# WAP to convert binary num  to decimal

num = int(input("enter a binary num  "))
temp = num
power = dec = 0

while num != 0:
    digit = num % 10 
    dec += (2**power) * digit
    num = num//10
    power += 1
    
print("decimal num of {} is {}.".format(temp,dec))

####################################################################################################################

# WAP to conver a str binary number to decmil

num = input("enter a binary num  ")
dec = 0
for i in range(len(num)-1,-1,-1):
    dec += int(num[i]) * (2**(len(num)-i-1))
print(dec)

####################################################################################################################
    
    