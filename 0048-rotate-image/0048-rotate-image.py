class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        #flip
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        
        for i in range(n//2):
            for j in range(i, m-i): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n//2):
            for j in range(i, m-1-i): 
                ii = n-1-i
                jj = m-1-j
                matrix[ii][jj], matrix[jj][ii] = matrix[jj][ii], matrix[ii][jj]

            

                