class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split(" "))
        l = [item for item in l if item != ""]

        return " ".join(l[::-1])        
