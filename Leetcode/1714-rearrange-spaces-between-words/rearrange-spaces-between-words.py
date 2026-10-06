class Solution:
    def reorderSpaces(self, text: str) -> str:
        cnt = text.count(" ")
        words = text.split()
        n = len(words)
        
        if n == 1:
            return words[0] + (" " * cnt)
        
        sep = cnt // (n - 1)
        extra = cnt % (n - 1)
        
        return (" " * sep).join(words) + (" " * extra)
