class Solution:
    def subarrayBitwiseORs(self, A: list[int]) -> int:
        res = set()
        cur = set()
        for num in A:
            cur = {num | x for x in cur} | {num}
            res |= cur
        return len(res)
