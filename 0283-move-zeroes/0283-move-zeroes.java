class Solution {
    public void moveZeroes(int[] nums) {
        int last = 0;
        int len = nums.length;

        for (int i=0; i<len; i++) {
            if (nums[i] != 0) {
                int temp = nums[i];
                nums[i] = nums[last];
                nums[last] = temp;
                last++;
            }
        }
    }
}
