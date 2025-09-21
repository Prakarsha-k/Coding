class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    area += 4 * grid[i][j] + 2
                if i > 0:
                    area -= 2 * min(grid[i][j], grid[i-1][j])
                if j > 0:
                    area -= 2 * min(grid[i][j], grid[i][j-1])
        return area
