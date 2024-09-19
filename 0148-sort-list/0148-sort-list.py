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
    
    def merge(self, left, right): 
        head = ListNode()
        tmp = head
        while left and right: 
            if left.val <= right.val:
                tmp.next =  left
                left = left.next
            else: 
                tmp.next = right
                right = right.next
            tmp = tmp.next
        
        tmp.next = left if left else right
        return head.next
    

    
