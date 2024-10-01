class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1001] * n
        memo[-1] = 0
        for i in range(n-2, -1, -1): 
            count = nums[i]
            jump = 1 if count else 1001
            memo[i] = jump + min( memo[i+1:i+1+count] if memo[i+1:i+1+count] else [0] )
        print(memo)
        return memo[0]