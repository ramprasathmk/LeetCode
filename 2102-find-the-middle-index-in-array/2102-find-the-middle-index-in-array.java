class Solution {
    public int findMiddleIndex(int[] nums) {
        var totalSum = 0;
        for (var num: nums) {
            totalSum += num;
        }

        var leftSum = 0;
        for (var i = 0; i< nums.length; i++) {
            var rightSum = totalSum - leftSum - nums[i];
            if (leftSum == rightSum) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}