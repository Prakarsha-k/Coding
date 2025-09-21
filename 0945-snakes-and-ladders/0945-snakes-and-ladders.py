from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        def get_num(s):
            quot, rem = divmod(s-1, n)
            row = n - 1 - quot
            col = rem if (n - 1 - row) % 2 == 0 else n - 1 - rem
            return row, col

        visited = set()
        queue = deque([(1, 0)])
        while queue:
            pos, steps = queue.popleft()
            if pos == n * n:
                return steps
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > n * n:
                    continue
                r, c = get_num(next_pos)
                if board[r][c] != -1:
                    next_pos = board[r][c]
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, steps + 1))
        return -1
