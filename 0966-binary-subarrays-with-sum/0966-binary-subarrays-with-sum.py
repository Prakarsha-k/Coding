from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            ans += count[prefix_sum - goal]
            count[prefix_sum] += 1
        return ans
