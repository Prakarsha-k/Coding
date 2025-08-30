class Solution {
    public String longestPalindrome(String s) {
       if (s.isEmpty() || s.length()==0)
       {
        return "";
       }
       int start=0;int end=0;
       for (int i=0;i<s.length();i++)
       {
            int left=i;int right=i; //odd length
            while(left>=0 && right<s.length() && s.charAt(left)==s.charAt(right))
            {
                if ((right-left)>(end-start))
                {
                    start=left;
                    end=right;
                }
                left--;
                right++;
            }
                int l=i;int r=i+1;//even length
                while(l>=0 && r<s.length() && s.charAt(l)==s.charAt(r))
                {
                    if ((r-l)>(end-start))
                    {
                        start=l;
                        end=r;
                    }
                l--;
                r++;
            }
       }
       return s.substring(start,end+1);
    }
       
}