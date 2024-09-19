# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head)
    
    def merge_sort(self, node): 
        if not node or not node.next: 
            return node
        
        slow = fast = node
        prev = None
        while fast and fast.next: 
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        left = self.merge_sort(node)
        right = self.merge_sort(slow)
        return self.merge(left, right)
    
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
    

    
