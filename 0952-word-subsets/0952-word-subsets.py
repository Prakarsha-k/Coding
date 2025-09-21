from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for w in words2:
            freq = Counter(w)
            for c in freq:
                max_freq[c] = max(max_freq[c], freq[c])
        ans = []
        for w in words1:
            freq = Counter(w)
            if all(freq[c] >= max_freq[c] for c in max_freq):
                ans.append(w)
        return ans
