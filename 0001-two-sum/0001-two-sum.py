class Solution(object):
    def twoSum(self, nums, target):
        result=[]
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
                    break
        return result