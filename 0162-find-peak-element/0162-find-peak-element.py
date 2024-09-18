class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        if len(nums) == 2: 
            return 0 if nums[0] > nums[1] else 1

        n = len(nums)
        left, right = 0, len(nums)-1
        # maximum = 0
        while left <= right: 
            mid = left + (right - left) // 2 
            # if nums[mid] > nums[maximum]: 
            #     maximum = mid
            if mid > 0 and mid < n -1 and nums[mid-1] < nums[mid] > nums[mid+1]: 
                return mid
            
            if mid > 0 and nums[mid-1] > nums[mid]: 
                right = mid -1
            else: 
                left = mid +1
        
        return -1
                
