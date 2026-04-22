import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            k = (left + right) // 2
            temp_h = 0
            for pile in piles:
                temp_h = temp_h + math.ceil(pile/k)
            if temp_h > h:
                left = k + 1
            else:
                right = k
        return left
            