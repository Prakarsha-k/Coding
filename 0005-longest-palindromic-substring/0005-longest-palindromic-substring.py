class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s=="" or len(s)==0:
            return ""
        start,end=0,0
        for i in range(0,len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l)>end-start:
                    start,end=l,r
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l)>end-start:
                    start,end=l,r
                l-=1
                r+=1
        return s[start:end+1]
        