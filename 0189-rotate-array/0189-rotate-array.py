class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        temp1=[]
        temp2=[]
        temp1=nums[n-k:n]
        temp2=nums[0:n-k]
        nums[:]=temp1+temp2
        return nums