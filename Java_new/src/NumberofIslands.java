public class NumberofIslands {
    char [][] grid;
    public void dfs(char[][] grid, int i, int j) {
        int[][] locations = {{-1,0}, {1, 0}, {0, 1}, {0, -1}};
        for (int[] location: locations) {
            int ii = i+location[0];
            int jj = j+location[1];
            if (ii>=0 && ii< grid.length && jj>=0 && jj< grid[0].length && grid[ii][jj] == '1') {
                grid[ii][jj] = '2';
                dfs(grid, ii, jj);
            }
        }
    }
    public int numIslands(char[][] grid) {
        this.grid = grid;
        int output = 0;
        for (int i=0; i< grid.length;i++) {
            for (int j=0; j<grid[0].length;j++) {
                if (grid[i][j] == '1') {
                    output++;
                    grid[i][j] = '2';
                    dfs(grid, i, j);
                }

            }
        }
        return output;
    }
}
