class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                distinct_elements = set()
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        distinct_elements.add(grid[r][c])
                
                nums = sorted(list(distinct_elements))
                
                if len(nums) < 2:
                    ans[i][j] = 0
                    continue
                
                min_diff = float('inf')
                for idx in range(len(nums) - 1):
                    diff = nums[idx+1] - nums[idx]
                    if diff < min_diff:
                        min_diff = diff
                    
                ans[i][j] = min_diff
                
        return ans