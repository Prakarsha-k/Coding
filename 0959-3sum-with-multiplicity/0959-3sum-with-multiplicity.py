from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        from collections import Counter
        count = Counter(arr)
        nums = sorted(count)
        ans = 0
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i:]):
                y = y
                z = target - x - y
                if z < y:
                    continue
                if z not in count:
                    continue
                if x == y == z:
                    ans += count[x] * (count[x]-1) * (count[x]-2) // 6
                elif x == y != z:
                    ans += count[x] * (count[x]-1) // 2 * count[z]
                elif x < y and y == z:
                    ans += count[x] * count[y] * (count[y]-1) // 2
                elif x < y < z:
                    ans += count[x] * count[y] * count[z]
        return ans % MOD
