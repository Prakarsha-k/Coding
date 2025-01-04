class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s 
        rows=['']*numRows
        step,index=1,0
        for char in s:
            rows[index]=rows[index]+char
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index=index+step
        return "".join(rows)