class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count=0
        cur_count=0
        for num in nums:
            if num==1:
                cur_count+=1
                max_count=max(max_count, cur_count)
            else:
                cur_count=0
        return max_count