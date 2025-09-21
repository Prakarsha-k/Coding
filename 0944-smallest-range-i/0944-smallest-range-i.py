class Solution:
    def smallestRangeI(self, A: list[int], K: int) -> int:
        max_val = max(A)
        min_val = min(A)
        return max(0, (max_val - min_val) - 2 * K)
