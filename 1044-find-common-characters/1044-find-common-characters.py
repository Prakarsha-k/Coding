from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        res = Counter(words[0])
        for word in words[1:]:
            res &= Counter(word)
        return list(res.elements())
