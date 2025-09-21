from typing import List

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res = []
        while A > 0 or B > 0:
            if len(res) >= 2 and res[-1] == res[-2]:
                if res[-1] == 'a':
                    res.append('b')
                    B -= 1
                else:
                    res.append('a')
                    A -= 1
            else:
                if A >= B:
                    res.append('a')
                    A -= 1
                else:
                    res.append('b')
                    B -= 1
        return ''.join(res)
