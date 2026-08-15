class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #first rows
        for row in board:
            seen = set()
            for col in row:
                if col != ".":
                    if col in seen:
                        return False
                    seen.add(col)
        
        #cols
        new_board = list(map(lambda col: list(col), zip(*board)))

        for col in new_board:
            seen = set()
            for row in col:
                if row != ".":
                    if row in seen:
                        return False
                    seen.add(row)
        
        #3x3

        for row in range(3):
            for col in range(3):

                seen = set()

                for r in range(row * 3, row * 3 + 3):
                    for c in range(col * 3, col * 3 + 3):
                        value = board[r][c]

                        if value != ".":
                            if value in seen:
                                return False
                            seen.add(value)
        return True




