class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        
        n = min(n, 3)
        
        if n == 1:
            return 2
        
        if n == 2:
            return 3 if presses == 1 else 4
            
        if n == 3:
            if presses == 1:
                return 4
            elif presses == 2:
                return 7
            else:
                return 8
