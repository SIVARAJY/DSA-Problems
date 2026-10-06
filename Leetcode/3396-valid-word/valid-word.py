class Solution(object):
    def isValid(self, word):
        vow = "aeiouAEIOU"
        cons = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
        num = "1234567890"
        vcnt = 0
        ccnt = 0
        n = len(word)
        if n <3:
            return False
        for ch in word:
            if ch not in vow and ch not in cons and ch not in num:
                return False
            if ch in vow:
                vcnt+=1
            if ch in cons:
                ccnt+=1
        if vcnt>0 and ccnt>0:
            return True
        else:
            return False                    
        