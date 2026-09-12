class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums= nums+[-2147483648] 
        n+=1      
        for i in range(1,n-1):
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                return i
        return 0       
