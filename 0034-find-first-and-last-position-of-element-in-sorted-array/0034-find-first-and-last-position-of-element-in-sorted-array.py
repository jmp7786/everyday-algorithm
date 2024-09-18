class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: 
            return [-1, -1]
        # if len(nums) == 1: 
        #     if nums[0] == target: 
        #         return [0,0]
        #     else: 
        #         return [-1, -1]

        ans_left = ans_right = -1 

        
        if nums[0] == target: 
            ans_left = 0
        else: 
            left = 0
            right = len(nums)-1
            while left <= right: 
                mid = left + (right - left) // 2 
                # print(mid)
                if nums[mid] == target and mid > 0 and  nums[mid-1] < nums[mid]: 
                    ans_left = mid
                    # print(mid, left, right)
                    break
                if nums[mid] >= target: 
                    right = mid -1
                else:
                    left = mid +1


        if nums[-1] == target: 
            ans_right = len(nums)-1
        else:            
            left = 0
            right = len(nums)-1
            while left <= right: 
                mid = left + (right - left) // 2 
                
                if nums[mid] == target and mid < len(nums)-1 and nums[mid+1] > nums[mid]: 
                    ans_right = mid
                    # print(mid, left, right)
                    break
                if nums[mid] <= target: 
                    left = mid +1
                else:
                    right = mid -1
        


        return ans_left, ans_right


            
            
            
