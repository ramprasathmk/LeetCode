class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> nums = new ArrayList<>();
        for (int i=left; i<= right; i++) {
            if (isDivisible(i)) nums.add(i);
        }
        return nums;
    }

    public boolean isDivisible(int x) {
        int num=x;
        while (num>0) {
            int digit = num % 10;
            if (digit == 0 || x % digit != 0) return false;
            num /= 10;
        }
        return true;
    }
}