class Solution {
    public int maximumCount(int[] nums) {
        int pos = 0, neg = 0;

        for (int num: nums) {
            if (num == 0) {
                continue;
            } else if (num < 0) {
                neg++;
            } else {
                pos++;
            }
        }

        return Math.max(pos, neg);
    }
}