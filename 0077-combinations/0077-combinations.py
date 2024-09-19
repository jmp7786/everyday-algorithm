class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        result = []
        self.build(0, nums, k, [], result)
        return result


    def build(self, start, nums, k, path, result): 
        if len(path) == k:
            result.append(path[:])
            return 

        for i in range(start, len(nums)): 
            n = nums[i]
            path.append(n)
            self.build(i+1, nums, k, path, result)
            path.pop()
        
