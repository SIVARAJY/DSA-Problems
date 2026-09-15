from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Unpack sub-arrays directly into the set intersection method
        # This completely eliminates Python loop overhead
        return sorted(set(nums[0]).intersection(*nums[1:]))
