class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cnt = 0
        
        sum_x = [sum(x) for x in mat]
        sum_y = [sum(y) for y in list(zip(*mat))]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if sum_x[i] == 1 and sum_y[j] == 1:
                        cnt += 1

        return cnt