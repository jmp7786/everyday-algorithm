# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    k = -1
    result = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k 
        
        def check(node, k): 
            if self.result:
                return 

            if not node: 
                return  
            
            if node.left: 
                check(node.left, k)
            
            self.k -= 1
            if self.k == 0 :
                self.result = node.val
                return 

            if node.right: 
                check(node.right, k)

            

        check(root, k)
        return self.result
