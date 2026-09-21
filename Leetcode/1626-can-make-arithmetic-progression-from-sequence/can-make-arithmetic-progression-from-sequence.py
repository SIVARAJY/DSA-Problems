class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        n = len(arr)
        arr.sort()
        a = arr[0]
        cd = arr[n-1]-arr[n-2]
        for i in range(n):
            if arr[i]!= a + ((i+1)-1)*cd:
                return False
        return True