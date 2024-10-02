class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i = 0 
        j = 0
        k = 0 
        
        visited = set()
        def check(i, j, k): 
            if i == len(s1): 
                return s2[j:] == s3[k:]
            if j == len(s2): 
                return s1[i:] == s3[k:]
            if k == len(s3): 
                return False
            if (i, j, k) in visited:
                return 
            visited.add((i,j,k))

            if s1[i] == s3[k]: 
                result = check(i+1, j, k+1)
                if result: 
                    return result
            if s2[j] == s3[k]: 
                return check(i, j+1, k+1)
            
        return check(0,0,0)
            