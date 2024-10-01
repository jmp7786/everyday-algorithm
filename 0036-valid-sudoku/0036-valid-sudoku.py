class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_box(i,j): 
            m = set()
            for x in range(3): 
                for y in range(3): 
                    n = board[i+x][j+y]
                    if n != '.' and n not in m: 
                        m.add(n)
                    elif n in m: 
                        return False
            return True

        def check_row(i):
            m = set()
            for x in range(9): 
                n = board[i][x]
                if n != '.' and n not in m: 
                    m.add(n)
                elif n in m: 
                    return False
            return True

        def check_col(j): 
            m = set()
            for y in range(9): 
                n = board[y][j]
                if n != '.' and n not in m: 
                    m.add(n)
                elif n in m: 
                    
                    return False
            return True
        
        for i in range(9):
            if not check_row(i): 
                print(3, i)
                return False
            if not check_col(i):
                print(2)
                return False

        for i in range(9): 
            for j in range(9): 
                if i % 3 == 0 and j % 3 == 0: 
                    if not check_box(i,j): 
                        print(1)
                        return False

        return True
        
            
        

