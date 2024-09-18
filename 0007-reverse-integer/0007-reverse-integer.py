class Solution:
    def reverse(self, x: int) -> int:

        if not isinstance(x, int):
            raise Exception(f"Invalid user type for variable `x`")

        INT_MIN: int = -2**31
        INT_MAX: int = 2**31 - 1

        result: int = 0

        sign: int = -1 if x<0 else 1
        x: int = abs(x)

        while x != 0:
            digit = x % 10
            x = x // 10

            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result        
    