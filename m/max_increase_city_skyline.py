class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        maxSkyLR = [max(i) for i in grid]
        maxSkyUD = [max(i) for i in zip(*grid)]
        maxSum = 0 
        
        for i, x in enumerate(grid):
            for j, y in enumerate(grid[i]):
                maxSum += min(maxSkyUD[j] - y, maxSkyLR[i] - y)
        
        return maxSum
        
        #48ms, 82.86%
