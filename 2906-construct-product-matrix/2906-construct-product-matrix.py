class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flatten = [r for g in grid for r in g]
        
        prefix = [1 for _ in range(len(flatten))]
        suffix = [1 for _ in range(len(flatten))]

        for i in range(1, len(flatten)):
            prefix[i] = (prefix[i-1] * flatten[i-1]) % 12345
        
        for i in range(len(flatten)-1)[::-1]:
            suffix[i] = (suffix[i+1] * flatten[i+1]) % 12345

        flatten = [p * s % 12345 for p, s in zip(prefix, suffix)]
        
        res = []
        for i in range(0, len(flatten), n):
            res.append(flatten[i:i+n])
        
        return res 