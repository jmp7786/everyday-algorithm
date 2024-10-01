class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [float('inf')] * n
        memo[-1] = 0
        for i in range(n-2, -1, -1): 
            count = nums[i]
            jump = 1 if count else float('inf')
            memo[i] = jump + min( memo[i+1:i+1+count] if memo[i+1:i+1+count] else [0] )
        
        return memo[0] != float('inf')
            