# finding 1 to 100 num
num=100
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        
# using user input    
num=int(input("enter a number"))
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i) 
# using ternary operator    
num=int(input("enter a number"))
for i in range(1,num+1):  
    result= "fizzbuzz" if i%3==0 and i%5==0 else "fizz" if i%3==0 else "buzz" if i%5==0 else i
    print(result)
    