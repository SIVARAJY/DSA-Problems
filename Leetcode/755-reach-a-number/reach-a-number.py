class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        current_sum = 0
        
        while current_sum < target:
            k += 1
            current_sum += k
            
        while (current_sum - target) % 2 != 0:
            k += 1
            current_sum += k
            
        return k
