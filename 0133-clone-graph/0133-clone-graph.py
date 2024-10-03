"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self): 
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return node
        if node.val in self.visited : 
            return self.visited[node.val]
        
        new_node = Node(node.val, [])
        self.visited[node.val] = new_node

        if node.neighbors: 
            for neighbor in node.neighbors:
                finded_neighbor =  self.cloneGraph(neighbor)
                new_node.neighbors.append(finded_neighbor)
        
        return new_node