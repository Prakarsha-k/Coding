class Solution(object):
    def countElements(self, nums):
        if nums:
            nums.sort()
            max_ele = nums.count(max(nums)) 
            min_ele = nums.count(min(nums))  
        return len(nums[min_ele:len(nums)-max_ele]) 

        