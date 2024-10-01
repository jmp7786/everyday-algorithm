class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_board = [board[i][:] for i in range(len(board))]

        for i in range(len(board)): 
            for j in range(len(board[0])): 
                neighbors = [
                    (1,0),
                    (-1,0),
                    (0,1),
                    (0,-1), 
                    (1,1),
                    (1,-1), 
                    (-1,-1),
                    (-1,1), 
                ]
                neighbor_count = 0
                for ii, jj in neighbors: 
                    iii = ii +i
                    jjj = jj +j
                    if 0 <= iii < len(new_board) and 0 <= jjj < len(new_board[0]) and new_board[iii][jjj]: 
                        neighbor_count += 1
                
                if board[i][j] == 1 and neighbor_count < 2: 
                    board[i][j] = 0
                elif board[i][j] == 1 and (neighbor_count == 2 or neighbor_count == 3): 
                    board[i][j] = 1
                elif board[i][j] == 1 and neighbor_count > 3 : 
                    board[i][j] = 0 
                elif board[i][j] == 0 and  neighbor_count == 3: 
                    board[i][j] = 1
        #         print(i,j, neighbor_count)
        # print(new_board)
        # print(board)
        return board


                