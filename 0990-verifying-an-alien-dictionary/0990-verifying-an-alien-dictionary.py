from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            for a, b in zip(words[i-1], words[i]):
                if index[a] < index[b]:
                    break
                elif index[a] > index[b]:
                    return False
            else:
                if len(words[i-1]) > len(words[i]):
                    return False
        return True
