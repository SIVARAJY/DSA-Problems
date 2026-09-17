class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        return [int(digit) for digit in "".join(map(str, nums))]
