from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            rotate_a = rotate_b = 0
            for a, b in zip(A, B):
                if a != x and b != x:
                    return float('inf')
                elif a != x:
                    rotate_a += 1
                elif b != x:
                    rotate_b += 1
            return min(rotate_a, rotate_b)

        ans = min(check(A[0]), check(B[0]))
        return -1 if ans == float('inf') else ans
