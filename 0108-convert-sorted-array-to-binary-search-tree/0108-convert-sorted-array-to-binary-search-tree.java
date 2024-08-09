/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        int len = nums.length;
        if (len == 0) {
            return null;
        }
        int mid = 0;
        if (len % 2 == 1) {
            mid = nums.length / 2 ;
        } else {
            mid = nums.length / 2 -1;
        }
        TreeNode node = new TreeNode(nums[mid]);

        node.left = sortedArrayToBST(Arrays.copyOfRange(nums,0,mid));
        node.right = sortedArrayToBST(Arrays.copyOfRange(nums,mid+1,nums.length));

        
        return node;
    }
}