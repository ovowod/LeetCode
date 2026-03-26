class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check_horizontal(m, n, mat):
            total_sum = sum(sum(row) for row in mat)

            bottom_set = {}
            for r in range(m):
                for val in mat[r]:
                    bottom_set[val] = bottom_set.get(val, 0) + 1
            
            top_set = {}
            top_sum = 0
            
            for r in range(m - 1):
                for val in mat[r]:
                    bottom_set[val] -= 1
                    if bottom_set[val] == 0: del bottom_set[val]
                    top_set[val] = top_set.get(val, 0) + 1
                    top_sum += val
                bot_sum = total_sum - top_sum

                if top_sum == bot_sum: return True
                if top_sum > bot_sum:
                    diff = top_sum - bot_sum
                    if (r + 1 > 1 and n > 1):
                        if diff in top_set: return True
                    elif r + 1 == 1:
                        if diff == mat[0][0] or diff == mat[0][n-1]: return True
                    else:
                        if diff == mat[0][0] or diff == mat[r][0]: return True
                else:
                    diff = bot_sum - top_sum
                    if (m - 1 - r > 1 and n > 1):
                        if diff in bottom_set: return True
                    elif m - 1 - r == 1:
                        if diff == mat[m-1][0] or diff == mat[m-1][n-1]: return True
                    else:
                        if diff == mat[r+1][0] or diff == mat[m-1][0]: return True
            return False
        
        m, n = len(grid), len(grid[0])

        hori = check_horizontal(m, n, grid)
        vert = check_horizontal(n, m, list(zip(*grid)))

        return hori or vert
        


        
        


            
