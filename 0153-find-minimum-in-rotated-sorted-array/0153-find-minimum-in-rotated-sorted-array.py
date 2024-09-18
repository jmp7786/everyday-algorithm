class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) ==1: 
            return nums[0]

        
        if nums[-1] > nums[0]: 
            return nums[0]

        left, right = 0, len(nums)-1
        while left <= right: 
            mid = left + (right - left) // 2
            print(mid, left, right)
            # print(mid, nums[left], nums[right])
            if mid > 0 and nums[mid-1] > nums[mid]: 
                return nums[mid]
            if mid < len(nums)-1 and nums[mid] > nums[mid+1]: 
                return nums[mid+1]

            if nums[left] > nums[mid]: 
                right = mid-1
            else: 
                left = mid+1
        print(left, right)
        return -1