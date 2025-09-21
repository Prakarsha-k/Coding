class Solution:
    def fairCandySwap(self, A: list[int], B: list[int]) -> list[int]:
        sumA, sumB = sum(A), sum(B)
        setB = set(B)
        diff = (sumA - sumB) // 2
        for a in A:
            if a - diff in setB:
                return [a, a - diff]
