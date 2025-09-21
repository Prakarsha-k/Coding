from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        from itertools import permutations
        max_time = -1
        for h1, h2, m1, m2 in permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if 0 <= hour < 24 and 0 <= minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        if max_time == -1:
            return ""
        return f"{max_time//60:02d}:{max_time%60:02d}"
