from typing import List

class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for c in S:
            stack.append(c)
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack[-3:] = []
        return not stack
