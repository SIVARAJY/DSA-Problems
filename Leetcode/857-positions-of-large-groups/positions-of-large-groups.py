class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        res = []
        i=0
        while(i<len(s)):
            j=i
            while(j<len(s) and s[i]==s[j]):
                j+=1
            if(j-i)>2:
                res.append([i,j-1])
            i=j    
        return res        
