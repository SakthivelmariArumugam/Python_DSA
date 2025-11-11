nums=[3,4,4,7,8,10]
target=5
left=0 
right=len(nums)-1
floor=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        floor=nums[mid]
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        floor=nums[mid]
        left=mid+1
ceil=-1
left=0 
right=len(nums)-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]<=target:
         left=mid+1
    else:
        ceil=nums[mid]
        right=mid-1
print(floor)
print(ceil)
