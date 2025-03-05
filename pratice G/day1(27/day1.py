# Find the Second Largest Element
#       [3, 1, 4, 1, 5, 9]  → 5
# Write a function to return the second largest number in an array.

numbers = [3, 1, 4, 1, 5, 9]
(numbers.sort())
numbers.reverse()
print(numbers[0])

# output 5

numbers = [3 ]
if len(numbers)<2:
    print("none")
else:
    (numbers.sort())
    numbers.reverse()
    print(numbers[1])

# None

# without using methods
numbers = [3, 1, 4, 1, 5, 9]
if len(numbers)<2:
    print("none")
else:
    first,second=float("-inf"),float("-inf")
    for num in numbers:
        if num>first:
            second,first=first,num
        else:
            second=num
    print(second)

# output=5


n = [3, 1, 4, 1, 5, 9]
if len(n)<2:
    print("none")
else:
    first,second=float("-inf"),float("-inf")
    for num in n:
        if num > first:
            first,second=num,first
        else:
            second=num
    print(second)

#########################################################################

# Sum of All Elements
#        [1, 2, 3, 4] → 10 
# Write a function that returns the sum of all elements in an array.

numbers=[1, 2, 3, 4]
sum=0
for num in numbers:
    sum +=num
    # sum=sum+num (this is hoe the above line works)
print(sum)
# op=10

# second way usinng methods
numbers=[1, 2, 3, 4]
sum=sum(numbers)
print(sum)
# print(sum(numbers))(hers this combines both the above lines)
###############################################################
# Remove Duplicates from an Array
#        [1, 2, 2, 3, 4, 4, 5] → [1, 2, 3, 4, 5]
# Write a function to remove duplicate values from an array.

numbers=[1, 2, 2, 3, 4, 4, 5] 
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)

# oup [1, 2, 3, 4, 5]

numbers=[1, 2, 2, 3, 4, 4, 5] 
unique = list(set(numbers))
print(unique)
# oup [1, 2, 3, 4, 5]

################################################################
