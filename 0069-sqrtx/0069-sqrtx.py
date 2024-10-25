class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            M = (left + right) // 2
            M_squared = M * M
            if M_squared == x:
                return M
            elif M_squared < x:
                left = M + 1
            else: 
                right = M - 1

        return right
        