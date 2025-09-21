class Solution:
    def smallestRangeII(self, A: list[int], K: int) -> int:
        A.sort()
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            high = max(A[i] + K, A[-1] - K)
            low = min(A[0] + K, A[i+1] - K)
            res = min(res, high - low)
        return res
