class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r =  max(piles)
        k = r
        while l <= r:
            hours = 0
            mid = (l + r) // 2
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours > h:
                l = mid + 1
            else:
                k = min(k, mid)
                r = mid - 1
        return k