class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Perform binary search on a sorted list.

        Parameters
        ----------
        arr : list[int]
            A sorted list of integers.
        target : int
            The integer value to search for.

        Returns
        -------
        int
            The index of target if found, otherwise -1.

        Notes
        -----
        - Time Complexity: O(log n)
        - Space Complexity: O(1)
        - Works for arrays of any length, including 0 or 1.
        """

        min_idx: int = 0
        max_idx: int = len(nums) - 1

        while ( min_idx <= max_idx ):
            mid: int = min_idx + (max_idx - min_idx) // 2

            if ( target == nums[mid] ): 
                return mid
            
            elif ( target > nums[mid] ): 
                min_idx = mid + 1
            
            else:
                max_idx = mid - 1

        return -1

        