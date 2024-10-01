class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        nums.sort()
        result = 0
        i = 0
        while i < len(nums):
            n = nums[i]
            x = n+1
            count = 1
            while x in s: 
                x +=1
                count +=1
                i+=1
            
            result = max(count, result)
            i+=1
        
        return result

            
