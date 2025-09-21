class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        xy = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        xz = sum(max(row) for row in grid)
        yz = sum(max(col) for col in zip(*grid))
        return xy + xz + yz
