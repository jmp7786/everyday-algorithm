class Solution {
    public int jump(int[] nums) {
        int minimum = nums.length-1;
        int[] dp = new int[nums.length];
        Arrays.fill(dp, nums.length); 
        dp[nums.length-1] = 0;

        for (int i = nums.length-2; i >=0; i--){
            int currMin = nums.length;
            for (int j = 1; j <= nums[i]; j++){
                if (i+j > nums.length-1) {
                    break;
                }
                currMin = Math.min(currMin, dp[i+j]);
            }
            dp[i] = currMin+1;
        }

        // System.out.println(Arrays.toString(dp));

        return dp[0];
    }
}