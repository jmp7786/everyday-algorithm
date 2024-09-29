"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None
    
        origin_memo = []
        memo = []
        node_map = {}
        curr = head
        while curr: 
            node = Node(curr.val)
            if curr.random:
                node.random = curr.random
                if curr.random not in node_map.keys(): 
                    node_map[curr.random] = [node]

            memo.append(node)
            origin_memo.append(curr)
            curr = curr.next

        curr = head

        x = [(k, v) for k, v in node_map.items()]
        print(x)
        for i in range(len(memo)): 
            if memo[i].random:
                memo[i].random = memo[origin_memo.index(memo[i].random)]

        for i in range(1, len(memo)): 
            memo[i-1].next = memo[i]
        
        return memo[0]
            
