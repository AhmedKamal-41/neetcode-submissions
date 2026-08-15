class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #loop over row by col
        for row in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[row][j] == ".":
                    continue
                if board[row][j] in seen:
                    return False
                seen.add( board[row][j])
        # loop over col by row
        for col in range(len(board)):
            seen = set()
            for i in range(len(board)):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add( board[i][col])


        for rowbox in range(3):         
            for boxcol in range(3):   
                seen = set()
                for i in range(3):     
                    for j in range(3):  
                        row = rowbox * 3 + i
                        col = boxcol * 3 + j
                        val = board[row][col]
                        if val != ".":  
                            if val in seen:
                                return False
                            seen.add(val)
        return True

            