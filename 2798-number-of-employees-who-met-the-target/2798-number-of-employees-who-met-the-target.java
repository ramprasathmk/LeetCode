class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int count = 0;
        
        for (int hh: hours) {
            if (hh >= target) {
                count++;
            }
        }

        return count;
    }
}