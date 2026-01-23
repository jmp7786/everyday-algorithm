class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val != ".":
                    row_marker = f"{val} in row {r}"
                    col_marker = f"{val} in col {c}"
                    box_marker = f"{val} in box {r//3}-{c//3}"
                    
                    if (row_marker in seen or 
                        col_marker in seen or 
                        box_marker in seen):
                        return False
                    
                    seen.add(row_marker)
                    seen.add(col_marker)
                    seen.add(box_marker)
                    
        return True
