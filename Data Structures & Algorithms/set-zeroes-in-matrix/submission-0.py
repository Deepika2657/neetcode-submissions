class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
           n=len(matrix)#rows
           m=len(matrix[0])#coloumns
           rows=[False]*n
           col=[False]*m
           for r in range(n):
             for c in range(m):
                if matrix[r][c]==0:
                    rows[r]=True
                    col[c]=True
           for r in range(n):
            for c in range(m):
                if rows[r] or col[c]:
                    matrix[r][c]=0
            


