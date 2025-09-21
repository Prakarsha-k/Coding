class Solution:
    def sumSubarrayMins(self, A: list[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        res = 0
        A = [0] + A + [0]
        
        for i, x in enumerate(A):
            while stack and A[stack[-1]] > x:
                mid = stack.pop()
                left = stack[-1]
                right = i
                res += A[mid] * (mid - left) * (right - mid)
                res %= MOD
            stack.append(i)
        
        return res
