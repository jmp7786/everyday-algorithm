class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.find(nums, [], set(), result)
        return result
    
    def find(self, nums, path, visited, result):         
        # print(path)
        if len(path) == len(nums): 
            result.append(path[:])
            return 
        
        for i in range(len(nums)): 
            n = nums[i] 
            if n not in visited:
                visited.add(n)
                path.append(n)
                self.find(nums, path, visited, result)
                path.pop()
                visited.remove(n)
        