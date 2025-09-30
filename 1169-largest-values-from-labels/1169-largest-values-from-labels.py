import heapq
from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        items = sorted(zip(values, labels), reverse=True)
        count = defaultdict(int)
        res = 0
        taken = 0
        for v, l in items:
            if taken == num_wanted:
                break
            if count[l] < use_limit:
                res += v
                count[l] += 1
                taken += 1
        return res
