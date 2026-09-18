class Solution:
    def isThree(self, n: int) -> bool:
        if n < 9:
            if n==4:
                return True
            return False
        
        root = int(math.isqrt(n))
        if root * root != n:
            return False
        
        if root % 2 == 0:
            return False
        
        for i in range(3, int(math.isqrt(root)) + 1, 2):
            if root % i == 0:
                return False   
        return True        