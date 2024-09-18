class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_maxs = [-1] * n
        right_maxs[-1] = nums[-1]
        suffix_sum = nums[-1]

        for i in range( n-2 , -1, -1): 
            suffix_sum += nums[i] 
            right_maxs[i] = max(right_maxs[i+1], suffix_sum)
        
        curr_max = nums[0]
        prefix_max = nums[0]
        special_max = nums[0]
        global_max =  nums[0]
        print(right_maxs)
        for i in range(1, n): 
            curr_max = max(curr_max, 0) + nums[i]
            global_max = max(global_max, curr_max)

            
            if i < n-1:
                special_max = max(special_max, prefix_max + right_maxs[i+1])
            prefix_max += nums[i] 
        return max(global_max, special_max)

