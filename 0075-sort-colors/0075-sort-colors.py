class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        low,mid,high=0,0,n-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            else:
                mid+=1
        return nums