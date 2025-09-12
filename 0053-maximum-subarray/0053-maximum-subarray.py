class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        total=0
        for i in range(0,len(nums)):
            total+=nums[i]
            max_sum=max(total,max_sum)
            if total<0:
                total=0
        return max_sum