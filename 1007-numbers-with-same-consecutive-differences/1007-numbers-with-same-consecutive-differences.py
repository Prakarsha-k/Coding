from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))
        res = []

        def dfs(num, length):
            if length == n:
                res.append(num)
                return
            last_digit = num % 10
            next_digits = set([last_digit + k, last_digit - k])
            for d in next_digits:
                if 0 <= d <= 9:
                    dfs(num * 10 + d, length + 1)

        for i in range(1, 10):
            dfs(i, 1)
        return res
