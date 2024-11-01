class Solution(object):
    def fib(self,n):
        n1=0
        n2=1
        if n==0:
            return 0
        if n==1:
            return 1
        # return self.fib(n-2)+self.fib(n-1)
        for i in range(2,n+1):      
           n3=n2+n1
           n1=n2
           n2=n3
        return n3
    
        