class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Flatten the board
        n = len(board)
        m = len(board[0])
        grid = [-1] * (n * m)
        
        index = 0
        flip = False
        for i in range(n-1, -1, -1):
            row = board[i]
            if flip:
                row.reverse()  # Reverse the row for zigzag traversal
            flip = not flip
            for cell in row:
                grid[index] = cell
                index += 1

        # Use BFS to find the shortest path
        from collections import deque
        queue = deque([(0, 0)])  # (position, moves)
        visited = set([0])

        while queue:
            pos, moves = queue.popleft()
            
            # If we reached the last cell
            if pos == len(grid) - 1:
                return moves
            
            # Explore next 6 possible moves
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos >= len(grid):
                    continue
                
                # If there's a ladder or snake, move to the target cell
                if grid[next_pos] != -1:
                    next_pos = grid[next_pos] - 1
                
                # Only process unvisited positions
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))

        return -1  # If no path is found