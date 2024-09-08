class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        maximum = 0
        for i in range(n): 
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    maximum = 1

        
        for i in range(1, n): 
            for j in range(1, m): 
                if dp[i][j] >= 1:
                    result = self.check(dp, i, j)
                    maximum = max(maximum, result)
                    
        return maximum * maximum
    
    def check(self, dp, i, j): 
        if dp[i-1][j-1] >= 1:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) +1 

        return dp[i][j]
        
        
        