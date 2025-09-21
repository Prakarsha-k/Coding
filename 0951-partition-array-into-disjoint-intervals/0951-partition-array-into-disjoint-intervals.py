from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        max_so_far = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] < left_max:
                left_max = max_so_far
                ans = i
            else:
                if nums[i] > max_so_far:
                    max_so_far = nums[i]
        return ans + 1
