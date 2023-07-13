class Solution(object):
    # Time complexity O(n^2)
    directions = [(0, 1), (0,-1),(1,0),(-1, 0)]

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0":
            return
        grid[i][j]="0"
        self.dfs(grid, i, j+1)
        self.dfs(grid, i+1, j)

        self.dfs(grid, i, j-1)
        self.dfs(grid, i-1, j)


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "0":
                    ans+=1
                    self.dfs(grid, i, j)
        return ans
    



