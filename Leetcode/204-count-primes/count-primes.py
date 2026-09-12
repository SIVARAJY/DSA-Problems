class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Sieve of Eratosthenes

        # We are only interested in numbers LESS than the input number
        # exit early for numbers LESS than 2; (two is prime)
        if n < 2:
            return 0
        
        # create strike list for the input range, initializing all indices to
        # prime (1).
        strikes = [1] * n

        strikes[0] = 0
        strikes[1] = 0
        
        for i in range(2, int(n**0.5)+1):
            if  strikes[i] != 0:
                strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)

        return sum(strikes)