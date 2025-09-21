from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_max = cur_min = 0
        max_sum = nums[0]
        min_sum = nums[0]
        for n in nums:
            cur_max = max(n, cur_max + n)
            max_sum = max(max_sum, cur_max)
            cur_min = min(n, cur_min + n)
            min_sum = min(min_sum, cur_min)
        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)
