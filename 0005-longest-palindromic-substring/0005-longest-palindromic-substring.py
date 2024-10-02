class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check(left, right): 
            while   0 <= left and  right <len(s) and  s[left] == s[right]: 
                left-=1
                right+=1
            return left+1, right-1

            
            
        result = 0, 0
        for i in range(1, len(s)): 
            left, right = check(i, i)
            if right-left > result[1] - result[0]: 
                result = left, right

            left, right = check(i-1, i)
            if right-left > result[1] - result[0]: 
                result = left, right
            check(i-1, i)
            print('result', result)
        
        return s[result[0]: result[1]+1]