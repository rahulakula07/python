# to converte the code from binary to decimal
num=int(input())
temp=num
count=dec=0
while num!=0:
    rem=num%10
    dec+=(2**count)*rem
    count+=1
    num //=10
print("decimal formate for{}is {}".format(temp,dec))
#########################################################################################################
# to convert the decinal into binary
num=int(input())
temp=num
binary=""
while num!=0:
    rem=num%2
    binary=str(rem)+binary
    num //=2
print("decimal formate for{}is {}".format(temp,binary))
#########################################################################################################
    





