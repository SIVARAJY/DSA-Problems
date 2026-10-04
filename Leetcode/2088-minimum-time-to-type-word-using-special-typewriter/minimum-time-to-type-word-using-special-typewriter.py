class Solution(object):
    def minTimeToType(self, word):
        ans = len(word)
        
        prev_char = 'a'
        
        for char in word:
            diff = abs(ord(char) - ord(prev_char))
            
            ans += min(diff, 26 - diff)
            
            prev_char = char
            
        return ans
