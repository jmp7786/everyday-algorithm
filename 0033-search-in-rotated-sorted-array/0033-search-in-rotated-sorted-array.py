class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1 
        # find minimum
        minimum_idx = -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        if nums[-1] > nums[0]: 
            minimum_idx = 0
        else : 
            left, right = 0, len(nums)-1
            while left <= right: 
                mid = left + (right - left) // 2
                if mid > 0 and nums[mid-1] > nums[mid]: 
                    minimum_idx = mid
                    break
                if mid > 0 and nums[mid] > nums[mid+1]: 
                    minimum_idx = mid+1
                    break
                
                if nums[left] > nums[mid]: 
                    right = mid-1
                else:
                    left = mid+1
        left, right = minimum_idx, minimum_idx + len(nums)-1
        n = len(nums)
        while left <= right: 
            mid = left + (right - left) // 2
            print(mid, mid%n)
            if nums[mid%n] == target: 
                ans = mid%n
                break
            
            if nums[mid%n] > target: 
                right = mid-1
            else:
                left = mid+1
        print(minimum_idx, ans)
        return ans


            
                    