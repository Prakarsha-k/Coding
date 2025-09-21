from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque
        deck.sort()
        q = deque()
        for card in reversed(deck):
            if q:
                q.appendleft(q.pop())
            q.appendleft(card)
        return list(q)
