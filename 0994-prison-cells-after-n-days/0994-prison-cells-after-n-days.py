from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = {}
        while N > 0:
            state = tuple(cells)
            if state in seen:
                N %= seen[state] - N
            seen[state] = N
            if N == 0:
                break
            N -= 1
            cells = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1, 7)] + [0]
        return cells
