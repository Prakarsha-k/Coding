class Solution:
    def minEatingSpeed(self, piles: list[int], H: int) -> int:
        left, right = 1, max(piles)
        
        def canEat(k):
            hours = 0
            for pile in piles:
                hours += -(-pile // k)  # Ceiling division
            return hours <= H
        
        while left < right:
            mid = (left + right) // 2
            if canEat(mid):
                right = mid
            else:
                left = mid + 1
        return left
