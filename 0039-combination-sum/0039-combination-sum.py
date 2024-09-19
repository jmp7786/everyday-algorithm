class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.find(0, candidates, target, 0, [], result)
        return result
    
    def find(self, start:int, candidates: List[int], target:int, amount: int, path: List[int], result:List[List[int]]): 
        if amount > target: 
            return 
        if amount == target: 
            result.append(path[:])
        
        for i in range(start, len(candidates)): 
            n = candidates[i]
            path.append(n)
            self.find(i, candidates, target, amount + n, path, result)
            path.pop()
        
