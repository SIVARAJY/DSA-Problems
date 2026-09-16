class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n= len(mat)
        j=n-1
        for i in range(n):
            sum+=mat[i][i]
            if i!=j:
                sum+=mat[i][j]
            j-=1
        return sum    

