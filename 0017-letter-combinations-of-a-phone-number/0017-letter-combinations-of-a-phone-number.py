class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return digits

        result = []
        table = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }

        def dfs(nums: str, path: str):
            if len(digits) == len(path): 
                result.append(path)
                return 

            for i in  range(len(nums)):
                for char in table[nums[i]]: 
                    dfs(nums[i+1:], path + char)
        
        dfs(digits, '')
        return result
