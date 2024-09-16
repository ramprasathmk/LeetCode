class Solution:

    def romanToInt(self, s: str) -> int:
        roman_map: dict[str, int] = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        total: int = 0
        prev_value: int = 0

        for char in s:
            current_value = roman_map[char]

            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value

        return total