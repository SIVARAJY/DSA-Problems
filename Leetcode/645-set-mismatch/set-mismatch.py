class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                rep=nums[i]
                break
        
        h2 = sum(x for x in range(1,len(nums)+1))
        h1 = sum(list(set(nums)))

        return [rep,h2-h1]
