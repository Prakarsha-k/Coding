from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1001
        for num, start, end in trips:
            arr[start] += num
            arr[end] -= num
        cur = 0
        for x in arr:
            cur += x
            if cur > capacity:
                return False
        return True
