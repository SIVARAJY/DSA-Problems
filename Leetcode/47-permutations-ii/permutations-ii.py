class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        return list(set(permutations(nums)))