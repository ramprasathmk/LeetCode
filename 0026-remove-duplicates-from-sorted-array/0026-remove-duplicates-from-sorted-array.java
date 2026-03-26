class Solution {
    public int removeDuplicates(int[] nums) {
        int len = nums.length;

        if (len == 0) return 0;

        int l = 0;
        int r = 1;

        while (r < len) {
            if (nums[r] != nums[l]) {
                l++;
                nums[l] = nums[r];
            }
            r++;
        }
        return l + 1;
    }
}