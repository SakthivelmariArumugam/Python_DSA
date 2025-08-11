List1=[7,8,9,1,2,3,4,5,6]
low=0
high=len(List1)-1
target=3
index=-1
while low<=high:
    mid=(low+high)//2
    if List1[mid]==target:
        index=mid
    if List1[low]<=List1[mid]:
        if List1[low]<=target and target<=List1[mid]:
            high=mid-1
        else:
            low=mid+1 
    else:
        if List1[mid]<=target and target<=List1[high]:
            low=mid+1 
        else:
            high=mid=-1
print(index)