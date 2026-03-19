class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        X = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        Y = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        cnt = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                X[i][j] = X[i][j-1] + X[i-1][j] - X[i-1][j-1]
                Y[i][j] = Y[i][j-1] + Y[i-1][j] - Y[i-1][j-1]

                if grid[i-1][j-1] == "X":
                    X[i][j] += 1
                elif grid[i-1][j-1] == "Y":
                    Y[i][j] += 1
                
                if X[i][j] == Y[i][j] and X[i][j] > 0:
                    cnt += 1
        return cnt