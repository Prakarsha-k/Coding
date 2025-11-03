class Solution {
    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        int m = grid.length, n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        dfs(grid, visited, row, col, grid[row][col]);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]) {
                    if (i == 0 || j == 0 || i == m - 1 || j == n - 1 ||
                        !visited[i - 1][j] || !visited[i + 1][j] ||
                        !visited[i][j - 1] || !visited[i][j + 1]) {
                        grid[i][j] = color;
                    }
                }
            }
        }
        return grid;
    }

    private void dfs(int[][] grid, boolean[][] visited, int i, int j, int val) {
        int m = grid.length, n = grid[0].length;
        if (i < 0 || j < 0 || i >= m || j >= n || visited[i][j] || grid[i][j] != val) return;
        visited[i][j] = true;
        dfs(grid, visited, i + 1, j, val);
        dfs(grid, visited, i - 1, j, val);
        dfs(grid, visited, i, j + 1, val);
        dfs(grid, visited, i, j - 1, val);
    }
}
