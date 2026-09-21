class Solution:
    def rob(self, nums: list[int]) -> int:
        curr = 0
        prev = 0
        for x in nums:
            temp = curr
            curr = max(curr,prev+x)
            prev = temp
        return curr    