class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=2
        cnt=0
        while k<len(s):
            if s[k]!=s[k-1] and s[k]!=s[k-2] and s[k-1]!=s[k-2]:
                cnt+=1
            k+=1
        return cnt        