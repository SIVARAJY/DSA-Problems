class Solution:
    def modifyString(self, s: str) -> str:
        l = list(s)
        
        for i in range(len(l)):
            if l[i] == '?':
                for char in ['a', 'b', 'c']:
                    prev_match = (i > 0 and l[i - 1] == char)
                    next_match = (i < len(l) - 1 and l[i + 1] == char)
                    
                    if not prev_match and not next_match:
                        l[i] = char
                        break 
                        
        return "".join(l)
