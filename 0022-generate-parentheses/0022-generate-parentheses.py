class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.build(n-1, n, '(', result)
        return result
    
    def build(self, on, off, string, result): 
        if on < 0 or off < 0:
            return 
        if on == 0 and off == 0 : 
            result.append(string)
            return 
        
        
        if on <= off: 
            self.build(on, off-1,  string+ ')', result)
            self.build(on-1, off,  string+ '(', result)
        else: 
            self.build(on, off-1,  string+ ')', result)

            