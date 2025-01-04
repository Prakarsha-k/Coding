class Solution(object):
    def isPalindrome(self, s):
        li1=[]
        li2=[]
        for item in s:
            if item.isalnum():
                li1.append(item.lower())
        n=len(li1)
        if n==0:
            return True
        li2=list(reversed(li1))
        for i in range(n):
            if li1[i]!=li2[i]:
                return False
        return True


