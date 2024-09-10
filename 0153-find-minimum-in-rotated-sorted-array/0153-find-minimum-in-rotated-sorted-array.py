class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[len(nums)-1]: 
            return nums[0]

        left = 0 
        right = len(nums)-1 
        while left < right: 
            mid = left + (right-left) // 2
            if nums[mid-1] >  nums[mid]: 
                return nums[mid]
            if nums[mid] >  nums[mid+1]: 
                return nums[mid+1]
            
            if nums[mid] > nums[left]: 
                left = mid +1
            else: 
                right = mid -1 
        
        return 0
            

