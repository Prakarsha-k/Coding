class Solution(object):
    def removeElement(self, nums, val):
        ele = 0  
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ele] = nums[i]
                ele += 1
        
        return ele