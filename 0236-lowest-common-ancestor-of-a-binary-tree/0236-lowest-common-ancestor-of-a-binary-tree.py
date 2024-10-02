# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node, target, path):
            if not node: 
                return node 
            # print('node', node)
            # print('node', node.val)
            # print('paths', [i.val for i in path])
            path.append(node)
            path_len = len(path)
            if node == target: 
                return node 
            left = find(node.left, target, path)
            if left: 
                return left
            while len(path) > path_len: 
                print('path.pop() left', path.pop())

            right = find(node.right, target, path)
            if right: 
                return right
            while len(path) > path_len: 
                print('path.pop() right', path.pop())
            return None

        p_path = [root]
        q_path = [root]

        if root == p or root == q: 
            return root

        
        finded_p = find(root.left, p, p_path)
        if not finded_p:
            p_path = [root]
            finded_p = find(root.right, p, p_path)
        # print('finded_p', finded_p)
        # print('p_path', p_path)
        # print()
        finded_q = find(root.left, q, q_path)
        if not finded_q: 
            q_path = [root]
            finded_q = find(root.right, q, q_path)
        # print('finded_q', finded_q)
        # print('q_path', q_path)

        if len(p_path) < len(q_path): 
            p_path, q_path = q_path, p_path
        
        # print('paths 1', [i.val for i in p_path])
        # print('paths 2', [i.val for i in q_path])

        for i in range(len(q_path)-1, -1, -1): 
            if p_path[i] == q_path[i]: 
                print(q_path[i])
                return q_path[i]
        # print('None')
        return None

        