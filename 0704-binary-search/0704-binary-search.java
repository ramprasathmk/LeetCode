class Solution {
    public int search(int[] arr, int target) {
        int min = 0;
        int max = arr.length - 1;

        while (min <= max) {
            int mid = min + (max - min ) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) min = mid + 1;
            else max = mid - 1; 
        }

        return -1;
    }
}