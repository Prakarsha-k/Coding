class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        num = 0
        for length in range(1, K + 1):
            num = (num * 10 + 1) % K
            if num == 0:
                return length
        return -1
