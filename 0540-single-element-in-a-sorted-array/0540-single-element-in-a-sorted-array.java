class Solution {
    public int singleNonDuplicate(int[] nums) {
        int result = 0;
        
        for (var num: nums) {
            result = result ^ num;
        }
        
        return result;
    }
}