class Solution(object):
    def isPalindrome(self, s):
        self.li1=[]
        self.li2=[]
        for item in s:
            if item.isalnum():
                self.li1.append(item.lower())
        self.n=len(self.li1)
        if self.n==0:
            return True
        self.li2=list(reversed(self.li1))
        for i in range(self.n):
            if self.li1[i]!=self.li2[i]:
                return False
        return True


