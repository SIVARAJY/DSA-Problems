class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s=str(n)
        if str(x) in s and s[0]!=str(x):
            return True
        else:
            return False