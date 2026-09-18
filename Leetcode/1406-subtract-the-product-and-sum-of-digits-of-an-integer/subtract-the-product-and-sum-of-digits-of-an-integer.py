class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = [int(digit) for digit in str(n)]
        return math.prod(l) - sum(l)
