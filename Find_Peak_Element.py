class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return 0
        while left<=right:
            mid=(left+right)//2
            if nums[left]>nums[left+1]:
                return left
            elif nums[right]>nums[right-1]:
                return right
            elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]>nums[mid]:
                right=mid-1
            else:
                left=mid+1

        return mid      
