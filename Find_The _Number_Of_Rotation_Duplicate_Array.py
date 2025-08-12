import sys
list1=[3,4,5,5,5,1,2,3,2,2,2]
min_value=sys.maxsize
min_index=-1
low=0
high=len(list1)-1
while low<=high:
    mid=(low+high)//2
    if list1[low]==list1[mid] and list1[mid]==list1[high]:
        low=low+1 
        high=high-1
    if list1[low]<=list1[mid]:
        if list1[low]<=min_value:
            min_value=list1[low]
            min_index=low
        low=mid+1 
    else:
        if list1[mid]<=min_value:
            min_value=list1[mid]
            min_index=mid 
        high=mid-1
print(min_index)
            