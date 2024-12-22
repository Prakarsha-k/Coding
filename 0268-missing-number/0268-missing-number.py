class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        t_sum = n * (n + 1) // 2  # Sum of n numbers 
        ele_sum = sum(nums)       # Sum of elements in array
        return t_sum - ele_sum
        
        