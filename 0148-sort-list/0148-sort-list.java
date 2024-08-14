/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode mid = getMid(head);
        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        return merge(left, right);
    }

    private ListNode getMid(ListNode node){
        ListNode slow = node;
        ListNode prev = null;
        while(node != null && node.next != null) {
            prev = slow;
            slow = slow.next;
            node = node.next.next;
        }
        prev.next = null;
        return slow;
    }

    private ListNode merge(ListNode left, ListNode right) {
        ListNode head = new ListNode(); 
        ListNode node = head;
        while(left != null && right != null){
            if(left.val < right.val) {
                node.next = left;
                left = left.next;
            } else {
                node.next = right;
                right = right.next;
            }
            node = node.next;
        }
        node.next = left != null ? left : right;
        return head.next;
    }
}