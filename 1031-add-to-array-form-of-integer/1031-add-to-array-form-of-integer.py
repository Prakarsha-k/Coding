from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        i = len(num) - 1
        carry = 0
        while i >= 0 or k > 0 or carry:
            n = num[i] if i >= 0 else 0
            n += k % 10 + carry
            res.append(n % 10)
            carry = n // 10
            k //= 10
            i -= 1
        return res[::-1]
