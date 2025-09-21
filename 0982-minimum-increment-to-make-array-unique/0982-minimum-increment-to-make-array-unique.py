from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                inc = nums[i-1] - nums[i] + 1
                nums[i] += inc
                ans += inc
        return ans
