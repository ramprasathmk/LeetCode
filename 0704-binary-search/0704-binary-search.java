class Solution {
    public int search(int[] nums, int target) {
        // Ensure that the array is in sorted order
        Arrays.sort(nums);

        // Actual Binary serach logic
        int min = 0;
        int max = nums.length - 1;

        while (min <= max) {
            int mid = min + (max - min) / 2;

            if (target == nums[mid]) return mid; 
            else if (target > nums[mid]) min = mid + 1;
            else max = mid - 1;
        }

        // If not found return -1
        return -1;
    }
}