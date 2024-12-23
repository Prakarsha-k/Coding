class Solution(object):
    def singleNumber(self, nums):
        count = {}
        for ele in nums:
            count[ele] = count.get(ele, 0) + 1
        for ele, freq in count.items():
            if freq == 1:
                return ele
