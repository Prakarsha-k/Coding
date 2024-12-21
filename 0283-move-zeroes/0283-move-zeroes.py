class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0  
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums