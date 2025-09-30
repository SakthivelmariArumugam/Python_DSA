n=input()
s=1
sum=0
for i in range(len(n)-1,-1,-1):
    if n[i]=='0':
        sum=sum+(0*s)
    if n[i]=='1':
        sum=sum+(1*s)
    s=s*2

print(sum)
