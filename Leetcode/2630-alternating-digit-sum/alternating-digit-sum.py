class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l = list(str(n))
        sum=0
        for i in range(len(l)):
            if i==0 or i%2==0:
                sum+=int(l[i])
            else:
                sum-=int(l[i])

        return sum            