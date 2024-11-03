class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        new_nums=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if nums[i] not in new_nums:
                new_nums.append(nums[i])
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        
        return len(new_nums)
