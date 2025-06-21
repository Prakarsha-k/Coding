class Solution(object):
    def firstMissingPositive(self, nums):
        nums = sorted(set([num for num in nums if num > 0])) 
        expected = 1
        for num in nums:
            if num != expected:
                return expected
            expected += 1
        return expected