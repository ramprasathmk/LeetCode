class Solution {
    public int maxProfit(int[] a) {
        int length = a.length;
        
        if (a == null || length < 2) {
            return 0;
        }

        int minPrice = a[0];
        int maxProfit = 0;

        for (int i=0; i<length; i++) {
            int profit = a[i] - minPrice;
            maxProfit = Math.max(profit, maxProfit);
            minPrice = Math.min(minPrice, a[i]);
        }
        return maxProfit;
    }
}