class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)): 
            curr_max = max(curr_max, 0) + nums[i]
            global_max = max(global_max, curr_max)
        
        return global_max