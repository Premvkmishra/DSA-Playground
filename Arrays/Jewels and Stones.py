class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        Count = 0
        for stone in stones:
            if stone in s:
                Count += 1

        return Count