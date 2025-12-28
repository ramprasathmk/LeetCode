class Solution {
    public int countNegatives(int[][] grid) {
        return (int) Arrays.stream(grid)
                    .flatMapToInt(Arrays::stream)
                    .filter(val -> val < 0)
                    .count();
    }
}