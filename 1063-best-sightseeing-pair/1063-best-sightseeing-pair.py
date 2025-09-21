from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = values[0]
        ans = 0
        for j in range(1, len(values)):
            ans = max(ans, best + values[j] - j)
            best = max(best, values[j] + j)
        return ans
