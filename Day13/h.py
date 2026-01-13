import math
def minEatingSpeed(self, piles: List[int], h: int) -> int: # type: ignore
        def can_finish(k: int) -> bool:
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / k)
            return hours_needed <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left 