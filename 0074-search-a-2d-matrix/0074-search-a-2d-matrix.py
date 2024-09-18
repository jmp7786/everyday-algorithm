class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left, right = 0, n * m -1
        while left <= right: 
            mid = left + (right -left) // 2 
            
            curr = matrix[mid//m][mid%m]
            print(curr, mid, mid//m, mid%m)
            if curr == target: 
                return True
            if curr < target: 
                left = mid +1
            else: 
                right = mid -1
        
        return False
            