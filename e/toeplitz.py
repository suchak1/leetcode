class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        numDiags = numRows + numCols - 1
        
        def diag(start, matrix):
            x = start[0]
            y = start[1]
            val = matrix[x][y]
            
            while x < len(matrix) - 1 and y < len(matrix[0]) - 1:
                x += 1
                y += 1
                
                if val != matrix[x][y]:
                    return False
            return True
        
        for i, x in enumerate(matrix):
            if not diag([i, 0], matrix):
                return False
        
        for j, y in enumerate(matrix[0]):
            if j == 0:
                continue
            elif not diag([0, j], matrix):
                return False
        
        return True
                
        #48ms, 79.94%
