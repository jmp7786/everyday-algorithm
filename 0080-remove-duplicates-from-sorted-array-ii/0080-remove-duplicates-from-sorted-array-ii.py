class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = None
        i = 0
        j = 0
        # print(n)
        while i < n: 
            t = nums[i]
            # print('nums[i]', i, nums[i], t)
            if k is None  or k != t : 
                # print('k, t',k, t)
                k = nums[i]
                nums[j] = k
                j+=1
                i+=1
            else:
                nums[j] = t
                # print('nums', nums[i], t)
                while i < n and nums[i] == t: 
                    i+=1
                j +=1
                k = None

            
            

        
        return j
            

            
            