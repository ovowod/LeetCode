class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        cnt = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_sum[i][j] = pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1] + grid[i-1][j-1]
                if pre_sum[i][j] <= k:
                    cnt += 1
        return cnt
        