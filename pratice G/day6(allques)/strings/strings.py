# Reverse a String
#       "hello" → "olleh"
# Write a function to reverse a given string.

# WIth SLICING METHOD
string=input("enter")
string[::-1]
print(string)
# OUTPUT
# hello
# olleh
str=input()
rev=""
for char in str:
    rev=char+rev
    print(rev)
print(rev)
# OUTPUT
# hello
# h
# eh
# leh
# lleh
# olleh
# olleh
str=input()
print("".join(reversed(str)))
# OUTPUT
# hello
# olleh
########################################################################
# Count Vowels in a String
#        "hello world" → 3
# Write a function to count the number of vowels in a given string.

str=input()
vowels="aeiouAEIOU"
count=0
for char in str:
    if char in vowels:
        count+=1
print(count)
# output
# Hello WORLD
# 3
############################################################################
# Remove Vowels from a String
#        "hello world" → "hll wrld"
# Write a function to remove all vowels from a given string.

str=input()
vowels="aeiouAEIOU"
res=""
for char in str:
    if char not in vowels:
        res+=char
print(count)
# output
# Hello World
# Hll Wrld.
################################################################################
# Convert String to Title Case
#        "hello world" → "Hello World"
# Write a function that converts a string to title case (capitalize the first letter of each word).

str=input()
print(str.title())
# output
# hello world
# Hello World 
str1=input().split()
cap=[word[0].upper()+word[1:] for word in str1]
print(" ".join(cap))
# output
# hello worls
# Hello Worls
######################################################################################
