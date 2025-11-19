class Solution {
    public int findFinalValue(int[] nums, int original) {
        Arrays.sort(nums);
        for (var elem: nums) {
            if (original == elem) {
                original *= 2;
            }
        }
        return original;
    }
}