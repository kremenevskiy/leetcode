class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        for i in range(1, n):
            grid[i][0] += grid[i-1][0]
        for j in range(1, m):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[n-1][m-1]



grid = [[1,3,1],[1,5,1],[4,2,1]]
ans = 7
assert Solution().minPathSum(grid) == ans


grid = [[1,2,3],[4,5,6]]
ans = 12
assert Solution().minPathSum(grid) == ans