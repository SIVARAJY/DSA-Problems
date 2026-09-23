class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        

        digit_freq: dict[int, int] = {}

        for digit in str(n): 
            if int(digit) in digit_freq: 
                digit_freq[int(digit)] += 1
            else: 
                digit_freq[int(digit)] = 1 

        output: int = 0 

        for key in digit_freq: 
            output += key * digit_freq[key]

        return output 