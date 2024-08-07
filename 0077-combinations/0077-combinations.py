class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(path: List[int], start: int): 
            if k < len(path): 
                return 
            if k == len(path): 
                result.append(path[:])
                return 
            
            for i in range(start, n+1): 
                path.append(i)
                dfs(path, i+1)
                path.pop()
        
        dfs([], 1)
        
        return result
