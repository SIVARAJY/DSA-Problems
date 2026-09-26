class Solution:
    def replaceDigits(self, s: str) -> str:
        l = list(s)
        l1 = ['1','2','3','4','5','6','7','8','9','0']
        for i in range(len(l)):
            if l[i] in l1:
                l[i]=chr(ord(l[i-1])+int(l[i]))
        return "".join(l)        