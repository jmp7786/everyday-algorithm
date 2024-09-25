class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def traversal(i, j, visited):
            if  0 <= i < len(board) and 0 <= j < len(board[0]) and (i,j) not in visited and board[i][j] == 'O': 
                board[i][j] = 'M'
                visited.add((i,j))

                traversal(i+1, j, visited)
                traversal(i-1, j, visited)
                traversal(i, j+1, visited)
                traversal(i, j-1, visited)
                
        
        for i in range(len(board)):
            traversal(i,0, set())
            traversal(i,len(board[0])-1, set())
        
        for j in range(len(board[0])):
            traversal(0,j, set())
            traversal(len(board)-1,j, set())
        
        # print(board)        
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if board[i][j] == "O": 
                    board[i][j] = "X"
                
                if board[i][j] == "M": 
                    board[i][j] = "O"
        
        return board