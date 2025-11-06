def subarray_sum(nums,target):
    k={}
    sum=0
    for i in range(len(nums)):
        sum=sum+nums[i]
        if sum==target:
            return [0,i]
        value=sum-target
        if value in k.keys():
            return [k[value]+1,i]
        else:
            k[sum]=i
    return []
   


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
