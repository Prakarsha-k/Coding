from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        ans = 0
        sorted_upto = [False] * (m - 1)
        for col in range(n):
            for row in range(m - 1):
                if not sorted_upto[row] and A[row][col] > A[row + 1][col]:
                    ans += 1
                    break
            else:
                for row in range(m - 1):
                    if A[row][col] < A[row + 1][col]:
                        sorted_upto[row] = True
        return ans
