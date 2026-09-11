class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle the edge case where either number is zero
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize an array to store the result digits
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Multiply from right to left (backwards)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                p1 = i + j
                p2 = i + j + 1
                
                total = mul + result[p2]
                
                result[p2] = total % 10
                result[p1] += total // 10
        
        string_result = [str(digit) for digit in result]
        
        start_idx = 1 if string_result[0] == '0' else 0
        
        return "".join(string_result[start_idx:])
