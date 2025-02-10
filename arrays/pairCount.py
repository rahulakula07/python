# the first line contains an int n, the num of scokes represent in arr
# the second line contain n spaces seprated int describing the color arr[i] of the scokes in the pile

# Input : 9
#         10 10 20 20 30 10 10 20 20


n = int(input())
num = input().split()
color = set(num)
pair = 0
for i in color:
    pair += num.count(i)//2
print(pair)