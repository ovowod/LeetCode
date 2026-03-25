class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + grid[i-1][j-1]

        if dp[m][n] % 2 != 0:
            return False

        if dp[m][n] // 2 in dp[m]:
            return True
        
        for i in range(m + 1):
            if dp[m][n] // 2 == dp[i][n]:
                return True
        
        return False