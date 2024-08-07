class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        i = 0 
        while i <= reach and i < len(nums): 
            reach = max(reach, i+nums[i])
            i +=1
        return reach >= len(nums)-1