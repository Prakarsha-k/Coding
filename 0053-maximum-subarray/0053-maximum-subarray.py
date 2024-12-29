class Solution(object):
    def maxSubArray(self, nums):
        max_sum = max(nums)
        current_sum = 0
    
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
        