class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        
        while right - left >= 0:
            middle = (left + right) // 2

            if len(matrix[middle]) and target < matrix[middle][0]:
                right = middle - 1
            elif len(matrix[middle]) and target > matrix[middle][len(matrix[middle]) - 1]:
                left = middle + 1
            else:
                return target in matrix[middle]
        
        return False
        
        #40ms, 79.01%
