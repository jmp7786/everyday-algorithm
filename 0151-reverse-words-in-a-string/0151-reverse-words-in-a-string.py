class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        n = len(s)

        for i in range(n//2): 
            print(i, n-1-i, n)
            s[i], s[n-1-i] = s[n-1-i], s[i]
        
        return ' '.join(s)