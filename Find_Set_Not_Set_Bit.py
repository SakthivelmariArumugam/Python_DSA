#find the ith bit in value is set or not set
n=int(input())
i=int(input())

#using left shift operator <<

if(n&(1<<i))!=0:
    print("set")
else:
    print("Not Set")

#using right shift operator >>

if((n>>i)&1)!=0:
    print("set")
else:
    print("Not Set")
