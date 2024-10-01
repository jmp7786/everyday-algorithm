class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        idx = 1
        q = deque()
        q.append(0)
        amount = nums[0]
        result = 1 if amount >= target else float('inf')
        while idx < len(nums): 
            q.append(idx) 
            amount += nums[idx]
            
            while amount >= target:
                result = min(result, len(q))
                i = q.popleft()
                amount -=nums[i]
            
            
            
                

            
            idx +=1
        return 0 if result == float('inf') else result
            

            