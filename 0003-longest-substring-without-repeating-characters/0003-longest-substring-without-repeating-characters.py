class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        m = {}
        result = 0
        for i in range(len(s)): 
            ch = s[i]
            if ch not in m: 
                m[ch] = i
            else: 
                idx = m[ch]
                # print('idx, ch',idx, ch, m, q)
                while q : 
                    ch_idx = q.popleft()
                    del m[s[ch_idx]]
                    if s[ch_idx]== ch:
                        break
                
                m[ch] = i
                # print('2, idx, ch',idx, ch, m, q)
            
            q.append(i)
            result = max(result, len(q))
        
        return result
