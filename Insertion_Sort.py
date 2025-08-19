nums=[13,46,24,52,20,9]
for i in range(0,len(nums)):
    j=i
    while j>0 and nums[j-1]>nums[j]:
        nums[j],nums[j-1]=nums[j-1],nums[j]
        j=j-1
print(nums)
#Time Complexity Of The Algorithm
#n+(n-1)+(n-2)+(n-3)+(n-n)=n(n+1)/2=n2/2+n/2 
#Remove the small value so n2/2 
# time complexity of the bubble sort o(n2)
