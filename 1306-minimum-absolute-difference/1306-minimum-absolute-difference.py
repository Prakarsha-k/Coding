from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = 10**18
        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            if d < mn:
                mn = d
        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == mn:
                res.append([arr[i-1], arr[i]])
        return res
