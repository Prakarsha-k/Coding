class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while(i<j):
            cur_sum=numbers[i]+numbers[j]
            if cur_sum==target:
                return [i+1,j+1]
            elif cur_sum>target:
                j-=1
            else:
                i+=1
        

