class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        g=max(candies)
        g1=[]
        for i in candies:
            if i+extraCandies>=g:
                g1.append(True)
            else:
                g1.append(False)
        return g1
        
        