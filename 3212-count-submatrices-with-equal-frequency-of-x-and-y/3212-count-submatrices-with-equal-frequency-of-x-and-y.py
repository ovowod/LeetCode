class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        cnt = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j][0] = dp[i][j-1][0] + dp[i-1][j][0] - dp[i-1][j-1][0]
                dp[i][j][1] = dp[i][j-1][1] + dp[i-1][j][1] - dp[i-1][j-1][1]
                if grid[i-1][j-1] == "X":
                    dp[i][j][0] += 1
                elif grid[i-1][j-1] == "Y":
                    dp[i][j][1] += 1
                
                if dp[i][j][0] > 0 and dp[i][j][0] == dp[i][j][1]:
                    cnt += 1
        
        return cnt