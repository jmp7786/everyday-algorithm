# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root
        self.path = []
        self.visited = set()

    def next(self) -> int:
        # print('next')
        # print('curr', self.curr)
        # print('path', self.path)
        # print('visited',  self.visited)
        
        result = self.curr.val
        if self.curr in self.visited and ((not self.curr.left and not self.curr.right ) or \
        (self.curr.left and self.curr.left in self.visited and self.curr.right and self.curr.right in self.visited) or \
        (self.curr.left and self.curr.left in self.visited and not self.curr.right) or \
        (not self.curr.left and self.curr.right and self.curr.right in self.visited)): 
            while self.path and self.path[-1] == self.curr: 
                self.path.pop()
            self.curr = self.path.pop()
            # print(self.curr.val)
            # print(self.visited)
            result = self.next()
            return result

        if not self.path or self.path and self.path[-1] != self.curr: 
            self.path.append(self.curr)

        if self.curr.left and self.curr.left not in self.visited: 
            self.curr = self.curr.left
            result = self.next()
        elif self.curr not in self.visited: 
            result = self.curr.val
            self.visited.add(self.curr)
        else: 
            self.curr = self.curr.right
            result = self.next()

        # print(result)
        # print()
        return result
        




    def hasNext(self) -> bool:
        # print('hasNext')
        # print(self.curr)
        # print(self.visited)
        # print(self.path)
        # print()
        if self.curr.left and self.curr.left not in self.visited: 
            return True
        if self.curr.right and self.curr.right not in self.visited: 
            return True
        if self.curr not in self.visited: 
            return True
        idx = -1
        while -len(self.path) <= idx and self.path[idx] in self.visited: 
                idx -= 1 
        if -len(self.path) <= idx:
            node_node = self.path[idx]
            if node_node not in self.visited:
                return True
        
        return False
        
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()