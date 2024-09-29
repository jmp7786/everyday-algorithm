# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tmp = None 
    last_right = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        def preorder(node): 
            if not node: 
                return node
            self.last_right = node
            tmp = node.right
                
            if node.left: 
                node.right = preorder(node.left)
            node.left = None

            if self.last_right:
                # print('self.last_right1',self.last_right)
                curr_last_right = self.last_right
                curr_last_right.right = preorder(tmp)
                # print('self.last_right2',self.last_right)
                

            # print(node)
            return node
        
        preorder(root)
        