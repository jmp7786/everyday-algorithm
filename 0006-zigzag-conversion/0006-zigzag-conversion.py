class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        matrix = []
        idx = 0 
        n = len(s)
        while idx < n:
            curr = [''] * numRows
            m = 0
            while idx < n and m < numRows: 
                # print(2)
                curr[m] = s[idx]
                idx +=1
                m +=1
            matrix.append(curr)
            x = numRows-1
            while idx < n and x > 1: 
                # print(1)
                curr = [''] * numRows
                curr[x-1] = s[idx]
                matrix.append(curr)
                x-=1
                idx +=1
            
        # print(matrix)
        for i in range(len(matrix[0])): 
            for j in range(len(matrix)): 
                result += matrix[j][i]

        # print(matrix)
        # print(result)
        return result



                
        