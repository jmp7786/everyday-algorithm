class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        rights = [float('-inf')] * n
        rights[-1] = nums[-1]
        rights_amount = nums[-1]
        for i in range(n-2, 0, -1):
            rights_amount += nums[i]
            rights[i] = max(rights_amount, rights[i+1])
        
        result = float('-inf')
        curr = float('-inf')
        left_result = float('-inf')
        left_amount = 0
        for i in range(n): 
            curr = max(curr+ nums[i], nums[i])
            result = max(result, curr)

            left_amount += nums[i]
            if i < n-1: 
                left_result = max(left_amount + rights[i+1], left_result)

        return max(left_result, result)