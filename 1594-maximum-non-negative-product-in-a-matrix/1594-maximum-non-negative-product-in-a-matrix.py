class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp_min = [[1 for _ in range(n)] for _ in range(m)]
        dp_max = [[1 for _ in range(n)] for _ in range(m)]

        dp_min[0][0] = dp_max[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp_min[i][0] = dp_max[i][0] = dp_min[i-1][0] * grid[i][0]
        
        for j in range(1, n):
            dp_min[0][j] = dp_max[0][j] = dp_min[0][j-1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp_min[i][j] = min(grid[i][j] * dp_min[i-1][j], grid[i][j] * dp_min[i][j-1], grid[i][j] * dp_max[i][j-1], grid[i][j] * dp_max[i-1][j])
                dp_max[i][j] = max(grid[i][j] * dp_min[i-1][j], grid[i][j] * dp_min[i][j-1], grid[i][j] * dp_max[i][j-1], grid[i][j] * dp_max[i-1][j])

        res = max(dp_min[m-1][n-1], dp_max[m-1][n-1])
        return res % (10 ** 9 + 7) if res >= 0 else -1