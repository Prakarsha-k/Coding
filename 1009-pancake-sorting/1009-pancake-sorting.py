from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            i = arr.index(size)
            if i != size - 1:
                if i != 0:
                    res.append(i + 1)
                    arr[:i + 1] = arr[:i + 1][::-1]
                res.append(size)
                arr[:size] = arr[:size][::-1]
        return res
