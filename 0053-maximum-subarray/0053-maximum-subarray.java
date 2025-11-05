class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int cur_sum = 0;
        int max_sum = Integer.MIN_VALUE;

        for (int i=0;i<n;i++) {
            cur_sum += nums[i];
            max_sum = (max_sum > cur_sum)?max_sum:cur_sum;
            if (cur_sum < 0) cur_sum = 0;
        }
        return max_sum;
    }
}