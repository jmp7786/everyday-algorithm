class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        def traversal(i, j, memo): 
            if i >= 0 and j >= 0 and i < len(obstacleGrid) and j < len(obstacleGrid[0]) and obstacleGrid[i][j] != 1 :
                if memo[i][j] != 0:
                    return memo[i][j]
                
                if i == len(obstacleGrid) -1 and j == len(obstacleGrid[0])-1:
                    memo[i][j] +=1 
                    return 1
                result = 0
                result += traversal(i+1, j, memo)
                
                result += traversal(i, j+1, memo) 
                memo[i][j] = result
                return result
            else: 
                return 0
            
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if n == 1 and m == 1:
            return 0 if obstacleGrid[0][0] else 1
        if obstacleGrid[0][0]:
            return 0 
        
        result = 0
        memo = [[0] * m for _ in range(n)]
        result += traversal(0, 1, memo)
        memo = [[0] * m for _ in range(n)]
        result += traversal(1, 0, memo)
        return result
    
    [
        [0,0,0,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,1,0],
        [0,0,0,0]
    ]