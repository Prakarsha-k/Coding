class Solution(object):
    def reverse(self, x):
        rev=0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        negative = x < 0
        if negative:
            if x == INT_MIN:
                return 0
            x = -x 
        while(x>0):
            rem=x%10
            if rev > (INT_MAX - rem) // 10:
                return 0
            rev=rev*10+rem
            x=x//10
        return -rev if negative else rev


x1=Solution()
print(x1.reverse(-121))
        