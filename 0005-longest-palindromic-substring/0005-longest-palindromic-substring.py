class Solution(object):
    def longestPalindrome(self, s):
        max_sub=s[0]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                cur_sub=s[i:j]
                rev_sub=cur_sub[::-1]
                if rev_sub==cur_sub and len(cur_sub)>len(max_sub):
                    max_sub=cur_sub             
        if (max_sub):
            return max_sub
        else:
            return ""

            
            
        