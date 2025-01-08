class Solution(object):
    def isHappy(self, n):
        seen = set()  
        while n != 1:
            sum1 = 0
            while n > 0:
                rem = n % 10
                sum1 += rem * rem 
                n = n // 10  
            if sum1 == 1:
                return True
            if sum1 in seen:
                return False 
            seen.add(sum1)  
            n = sum1  
        return True
