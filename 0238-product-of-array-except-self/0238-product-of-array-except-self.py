class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        memo = [1] * n 
        product = 1
        for i in range(1, n): 
            product *= nums[i-1]
            memo[i] = product
        
        print(memo)

        product = 1
        for i in range(n-2, -1, -1): 
            product *= nums[i+1]
            memo[i] = memo[i] * product
        
        return memo
        
        