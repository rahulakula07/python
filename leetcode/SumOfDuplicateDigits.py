# Write a program that takes a number as input, print the sum of duplicate numbers in the given number.

# Testcase1	:  7473183
# Output     	:  10
# Explanation	: In the given number 747383, duplicate digits are 7 and 3 because they occurred more than once in the number. So the sum of 7 and 3 are 10.

# Testcase1	:  234234
# Output     	:  9
# Explanation	: In the given number 234234, duplicate digits are 2, 3 and 4 because they occurred more than once in the number. So the sum of 2, 3 and 4 are 9.

s="7473183"
res=""
dup=[]
for i in s:
    if i not in res:
        res+=i
    else:
        dup+=[i]
# print(res)
print(dup)
sum=0
for i in dup:
    sum+=int(i)
print(sum)
