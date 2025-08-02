class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result: int = 0
        
        for num in nums:
            result ^= num
        
        return result
        