// BinarySearch performs binary search on a sorted slice.
// Returns the index of target if found, otherwise -1.
//
// Time Complexity: O(log n)
// Space Complexity: O(1)
// Works for slices of any length, including empty or single-element.
func search(nums []int, target int) int {
    min := 0
    max := len(nums) - 1

    for min <= max {
        mid := min + (max - min) / 2

        if target == nums[mid] {
            return mid
        } else if target > nums[mid] {
            min = mid + 1
        } else {
            max = mid - 1
        }
    }

    return -1
}