class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        
        for val, idx in zip(nums, index):
            target.insert(idx, val)
            
        return target
