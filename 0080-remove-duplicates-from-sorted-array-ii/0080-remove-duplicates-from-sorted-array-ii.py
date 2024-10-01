class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = None
        i = 0
        j = 0
        
        while i < n: 
            t = nums[i]
            if k is None  or k != t : 
                k = nums[i]
                nums[j] = k
                j+=1
                i+=1
            else:
                nums[j] = t
                while i < n and nums[i] == t: 
                    i+=1
                j +=1
                k = None
        
        return j
            

            
            