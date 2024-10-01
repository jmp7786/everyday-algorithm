class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n -1
        result = 0
        while left < right: 
            h = min(height[left], height[right])
            curr = h * (right-left)
            result = max(result, curr)
            if height[left] > height[right]: 
                right -=1
            else: 
                left +=1
        
        return result
