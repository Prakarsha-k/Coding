from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = 2
            q.append((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        q = deque()
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        steps = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return steps
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            q.append((nx, ny))
            steps += 1
        return -1
