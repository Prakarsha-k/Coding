class Solution(object):
    def plusOne(self, digits):
        digits1=int(''.join(map(str,digits)))
        sum_digits=digits1+1
        result = list(map(int, str(sum_digits)))
        return result
        