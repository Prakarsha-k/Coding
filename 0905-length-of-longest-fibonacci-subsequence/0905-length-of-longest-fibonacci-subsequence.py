class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        s = set(arr)
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                x, y = arr[i], arr[j]
                length = 2
                while x + y in s:
                    x, y = y, x + y
                    length += 1
                res = max(res, length if length > 2 else 0)
        return res
