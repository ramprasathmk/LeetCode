class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        jewels_count: int = 0
        
        for stone in stones:
            if stone in jewels:
                jewels_count += 1

        return jewels_count
        