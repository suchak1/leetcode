class Solution:
    
    def numPawns(self, line):
        for c in line:
            if c == ".":
                continue
            elif c == "p":
                return 1
            else:
                return 0
        return 0
            
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        pos = []
        
        for i, x in enumerate(board):
            for j, y in enumerate(x):
                if y == "R":
                    pos.append(i)
                    pos.append(j)
                    break
        i = pos[0]
        j = pos[1]
                    
        right = self.numPawns(board[i][j+1:])
        left = self.numPawns(board[i][:j][::-1])
        trans = [list(row) for row in zip(*board)]
        down = self.numPawns(trans[j][i+1:])
        up = self.numPawns(trans[j][:i][::-1])
       
        return left+right+up+down
        #36ms, 99.86%
