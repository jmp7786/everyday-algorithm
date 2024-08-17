/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
}
*/

class Solution {
    private boolean isLeaf(int[][] grid, int x1, int y1, int length) {
        int baseNum = grid[x1][y1];
        for (int i=0; i < length; i++) {
            for (int j=0; j < length; j++) {
                if(grid[i + x1][j + y1] !=  baseNum) {
                    return false;
                }
            }   
        }
        return true;
    }
    private Node solve(int[][] grid, int x1, int y1, int length) {
        if(isLeaf(grid, x1, y1, length)) {
            System.out.println(grid[x1][y1]);
            return new Node(grid[x1][y1] == 1, true);
        } else {
            Node node = new Node(false, false);
    
        node.topLeft = solve(grid, x1, y1, length/2);
        node.topRight = solve(grid, x1 , y1 + length / 2, length/2);
        node. bottomLeft = solve(grid, x1 + length / 2, y1, length/2);
        node. bottomRight = solve(grid, x1 + length / 2, y1 + length / 2, length/2);

            return node;
        }
    }

    public Node construct(int[][] grid) {
        return solve(grid, 0, 0, grid.length);
    }
}