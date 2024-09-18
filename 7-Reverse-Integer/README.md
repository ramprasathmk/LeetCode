# 7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


## Example 1:

- Input: x = 123
- Output: 321


## Example 2:

- Input: x = -123
- Output: -321


## Example 3:

- Input: x = 120
- Output: 21


## Constraints:

- -231 <= x <= 231 - 1


## Code Implementation:

```python
class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN: int = -2**31
        INT_MAX: int = 2**31 - 1

        result: int = 0

        sign: int = -1 if x<0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x // 10

            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result
```


## Explanation:
1. **Sign Handling**: The `sign` variable stores whether the number is positive or negative. We convert `x` to its absolute value to reverse the digits easily.
   
2. **Reversing**: The number is converted to a string, reversed using slicing (`[::-1]`), and then converted back to an integer.
   
3. **Overflow Check**: After reversing, the result is compared against the 32-bit integer limits. If it exceeds the valid range, the function returns `0`.
   
4. **Result**: The result is returned with the correct sign.


## Time Complexity:
- The time complexity is \(O(n)\), where \(n\) is the number of digits in the integer. The operations of reversing a string and checking for overflow both run in linear time with respect to the number of digits.


## Space Complexity:
- The space complexity is \(O(n)\) due to the space needed to store the reversed string.


## Runtime:
- **38**ms | Beats **44.18%**

## Memory:
- **16.72**MB | Beats **5.01%**
