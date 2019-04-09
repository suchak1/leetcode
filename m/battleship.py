class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
    
        lastRow = {}
        last = 0
        ships = 0

        for i, x in enumerate(board):
            thisRow = {}
            
            for j, y in enumerate(board[i]):
                if board[i][j] == "X":
                    thisRow[j] = 1
                    if j in lastRow or last == 1:
                        continue
                    else:
                        ships += 1
                        last = 1
                else:
                    last = 0


            lastRow = thisRow
            last = 0


        return ships
        
        #40ms, 78.39%
