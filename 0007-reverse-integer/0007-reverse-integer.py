class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN: int = -2**31
        INT_MAX: int = 2**31 - 1

        if not isinstance(x, int):
            raise Exception(f"Invalid Type, {x=} must be an Integer.")
        
        if x not in range(INT_MIN, INT_MAX+1):
            raise Exception(f"{x=} is not in [ {INT_MIN} <= x <= {INT_MAX} ]")

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
    
        