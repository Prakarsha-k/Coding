from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s='', open=0, close=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open < n:
                backtrack(s + '(', open + 1, close)
            if close < open:
                backtrack(s + ')', open, close + 1)
        backtrack()
        return res
