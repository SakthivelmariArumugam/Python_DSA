#check if the number is power of two:
n=int(input())
if n<1:
    print("The Number is Invalid")
elif n&(n-1)==0:
    print("The number is power of two")
else:
    print("The number is not power of two")
