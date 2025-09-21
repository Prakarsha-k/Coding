from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        def canShip(cap):
            need, cur = 1, 0
            for w in weights:
                if cur + w > cap:
                    need += 1
                    cur = 0
                cur += w
            return need <= days
        
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left
