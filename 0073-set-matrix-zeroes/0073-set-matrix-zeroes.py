class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        rows = []
        cals = []
        for i in range(n): 
            for j in range(m): 
                if matrix[i][j] == 0: 
                    rows.append(i)
                    cals.append(j)
        for i in rows: 
            matrix[i] = [0] * m
        
        for j in cals: 
            for i in range(n): 
                matrix[i][j] = 0
        
                

                    
        