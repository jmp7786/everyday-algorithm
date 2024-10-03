class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        i = 0 
        res = []
        for i in range(len(paths)): 
            s = paths[i]
            if s == '..': 
                if res:
                    res.pop()
            elif s != '.' and s != '': 
                res.append(s)
        
        print(res)
        return '/' + '/'.join(res)
            
            
                