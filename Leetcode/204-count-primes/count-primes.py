class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a boolean array tracking primality
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Loop up to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark multiples of i starting from i * i as false
                for j in range(i * i, n, i):
                    is_prime[j] = False
                    
        return sum(is_prime)
