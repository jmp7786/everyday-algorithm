"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def is_leaf(self, grid: List[List[int]], i: int, j: int, size:int) -> bool:
        print(i, j, size)
        curr = grid[i][j]
        for x in range(i, i + size): 
            for y in range(j, j+ size): 
                if grid[x][y] != curr: 
                    return False
        
        return True

    def construct(self, grid: List[List[int]]) -> 'Node':   
        i =  j = 0
        size = len(grid)
        node = self.construct_node(grid, i, j, size)
        print(node)
        return node

    def construct_node(self, grid: List[List[int]], i: int, j: int, size: int) -> 'Node':
        is_leaf = self.is_leaf(grid, i, j, size)
        print(is_leaf)
        if is_leaf: 
            # grid[i][j]
            node = Node(grid[i][j], True)
            return node
        
        node = Node(False, False)
        half = size // 2
        node.topLeft = self.construct_node(grid, i, j , half)
        node.topRight = self.construct_node(grid, i, j  + half, half)
        node.bottomLeft = self.construct_node(grid, i + half, j , half)
        node.bottomRight = self.construct_node(grid, i + half, j + half , half)
        return node
        

