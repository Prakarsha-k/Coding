from typing import List

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res, num = [], 0
        for bit in A:
            num = (num << 1 | bit) % 5
            res.append(num == 0)
        return res
