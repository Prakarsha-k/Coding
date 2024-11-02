class Solution(object):
    def check(self, nums):
        n=len(nums)
        new_nums=[]
        if n==1 or n==2:
            return True
    
        for k in range(n):
            new_nums=[]
            for i in range(n):
                new_nums.append(nums[(k+i)%n])
            is_sorted=True
            nn=len(new_nums)   
            for j in range(nn-1):
                if new_nums[j]>new_nums[j+1]:
                    is_sorted=False
                    break
            
            if is_sorted==True:
                return True
        return False
        
                 

    
        