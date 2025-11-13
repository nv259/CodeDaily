class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_row(board):
            for row_i in board:
                nums = set()
                for j in range(len(board[0])):
                    if row_i[j] == '.': continue
                    
                    if row_i[j] in nums:
                        return False
                    nums.add(row_i[j])
            
            return True
        
        def check_grid(board):
            for start_row in range(0, len(board), 3):
                for start_col in range(0, len(board[0]), 3):
                    nums = set()
                    
                    for i in range(start_row, start_row + 3):
                        for j in range(start_col, start_col + 3):
                            if board[i][j] == '.': continue
                            
                            if board[i][j] in nums:
                                return False
                            nums.add(board[i][j])

            return True
        
        row_valid = check_row(board)
        grid_valid = check_grid(board)
        # transpose board
        board = [[board[j][i] for j in range(len(board))] 
                 for i in range(len(board[0]))]
        col_valid = check_row(board)

        return row_valid and grid_valid and col_valid
