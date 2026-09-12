class Solution:
    def trailingZeroes(self, n: int) -> int:
        f=1
        five=5
        res=0
        while f==1:
            if(n//five>0):
                res+=n//five
                five*=5
            else:
                break
        return res        