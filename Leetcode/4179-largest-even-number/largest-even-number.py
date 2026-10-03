class Solution:
    def largestEven(self, s: str) -> str:
        c=0
        d=0
        for i in s:
            if i=='2':
                c=d+1
            d+=1
        if c:
            return s[:c]
        return ""

        