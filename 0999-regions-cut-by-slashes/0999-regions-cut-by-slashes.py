from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = {}
        
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0 or j == 0 or i == n or j == n:
                    parent[(i, j)] = (0, 0)
        
        ans = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    a = (i, j+1)
                    b = (i+1, j)
                elif grid[i][j] == '\\':
                    a = (i, j)
                    b = (i+1, j+1)
                else:
                    continue
                if find(a) == find(b):
                    ans += 1
                else:
                    union(a, b)
        return ans
