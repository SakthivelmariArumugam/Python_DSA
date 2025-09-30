n=int(input())
s=""
while n>0:
    k=n%2
    if k==0:
        s='0'+s
    if k==1:
        s='1'+s
    n=n//2

print(s)
    
