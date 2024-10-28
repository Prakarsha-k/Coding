class Solution: 
    def isPalindrome(self,n):
        temp=n
        rev=0
        while(n>0):
            rem=n%10
            rev=rev*10+rem
            n=n//10
        if temp==rev:
            return True
        else:
            return False

num1=Solution()  
result=num1.isPalindrome(121)
print(result)
        