class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        if len(nums)==1:
            return nums[0]
        if nums[low]!=nums[low+1]:
                return nums[low]
        if nums[high]!=nums[high-1]:
                return nums[high]
        while low<=high:
            mid=(low+high)//2
            if (nums[mid]!=nums[mid+1]) and (nums[mid]!=nums[mid-1]):
                return nums[mid]
            elif (mid%2!=0 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                low=mid+1
            else:
                high=mid-1
