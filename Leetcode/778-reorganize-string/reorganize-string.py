from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)
        
        sorted_chars = sorted(char_counts.items(), key=lambda x: -x[1])
        
        if sorted_chars[0][1] > (len(s) + 1) // 2:
            return ""
        
        res = [""] * len(s)
        idx = 0
        
        for char, count in sorted_chars:
            for _ in range(count):
                if idx >= len(s):
                    idx = 1  
                res[idx] = char
                idx += 2
                
        return "".join(res)
