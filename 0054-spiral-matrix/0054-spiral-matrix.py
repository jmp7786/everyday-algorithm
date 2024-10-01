class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        step = n//2 + n%2
        result = []
        visited = set()
        top = 0
        left = 0 
        right = m-1 
        bottom = n-1
        while top < bottom and left < right:

            for j in range(left, right+1): 

                result.append(matrix[top][j])
            
            
            for i in range(top+1, bottom): 
                result.append(matrix[i][right])
            

            for j in range(right, left-1, -1): 
                result.append(matrix[bottom][j])
            
            
            for i in range(bottom-1, top, -1): 
                result.append(matrix[i][left])
            left +=1
            top +=1
            bottom -=1
            right -=1
        
        if  top == bottom and left < right:
            for j in range(left, right+1): 
                result.append(matrix[top][j])
        elif  top < bottom and left == right:
            for i in range(top, bottom+1): 
                result.append(matrix[i][left])
        elif top == bottom and left == right:
            result.append(matrix[top][left])

        return result

                
                    