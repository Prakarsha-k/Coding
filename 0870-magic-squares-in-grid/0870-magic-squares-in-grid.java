class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int rows = grid.length, cols = grid[0].length, count = 0;
        for (int i = 0; i <= rows - 3; i++) {
            for (int j = 0; j <= cols - 3; j++) {
                if (isMagic(grid, i, j)) count++;
            }
        }
        return count;
    }
    
    private boolean isMagic(int[][] g, int r, int c) {
        int[] freq = new int[10];
        for (int i = r; i < r + 3; i++) {
            for (int j = c; j < c + 3; j++) {
                int val = g[i][j];
                if (val < 1 || val > 9 || freq[val]++ > 0) return false;
            }
        }
        int sum = g[r][c] + g[r][c+1] + g[r][c+2];
        for (int i = 0; i < 3; i++) {
            if (g[r+i][c] + g[r+i][c+1] + g[r+i][c+2] != sum) return false;
            if (g[r][c+i] + g[r+1][c+i] + g[r+2][c+i] != sum) return false;
        }
        if (g[r][c] + g[r+1][c+1] + g[r+2][c+2] != sum) return false;
        if (g[r][c+2] + g[r+1][c+1] + g[r+2][c] != sum) return false;
        return true;
    }
}
