class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        ds = ss = 0
        while n > 0:
            c = n%10
            n//=10
            ds+=c
            ss+=(c*c)
        return ss-ds >=50     
            