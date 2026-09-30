class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        current_string = ""
        
        for word in words:
            current_string += word
            
            if current_string == s:
                return True
            
            if len(current_string) > len(s):
                return False
                
        return False
