class checkmate:
    def __init__(self, chessboard):
        self.chessboard = chessboard

    def king_is_in_check(chessboard):
        # KING SETUP
        king = 'K'
        for row, s in enumerate(chessboard):
            for col, i in enumerate(s):
                if i == king:
                    king_row = row
                    king_col = col
        print([king_row,king_col])
        # OTHER PIECES DEFINED
        pawn = 'P'
        #knight = '♞'
        rook = 'R'
        bishop = 'B'
        queen = 'Q' 
    ##### PAWN CHECK
        if king_col>0:
            if chessboard[king_row-1][king_col-1] == pawn:
                return True
        if king_col<7:
            if chessboard[king_row-1][king_col+1] == pawn:
                return True
    ##### KNIGHT CHECK
        # up
        # if king_row > 1 and king_col>0:
        #     if chessboard[king_row-2][king_col-1] == knight:
        #         return True
        # if king_row > 1 and king_col<7:
        #     if chessboard[king_row-2][king_col+1] == knight:
        #         return True
        # right
        # if king_row > 0 and king_col < 6:
        #     if chessboard[king_row-1][king_col+2] == knight:
        #         return True
        # if king_row < 7 and king_col < 6:
        #     if chessboard[king_row+1][king_col+2] == knight:
        #         return True
        # down
        # if king_row < 6 and king_col <7:
        #     if chessboard[king_row+2][king_col+1] == knight:
        #         return True
        # if king_row < 6 and king_col > 0:
        #     if  chessboard[king_row+2][king_col-1] == knight:
        #         return True
        # left
        # if king_row < 7 and king_col > 1:
        #     if chessboard[king_row+1][king_col-2] == knight:
        #         return True
        # if king_row > 0 and king_col > 1:
        #     if chessboard[king_row-1][king_col-2] == knight:
        #         return True
    ##### ROOK CHECK + QUEEN
        # left horizontal
        for n in range(king_col-1,-1,-1):
            if chessboard[king_row][n] == rook or chessboard[king_row][n] == queen:
                return True
            elif chessboard[king_row][n] != ' ':
                break
        # right horizontal
        for n in range(king_col+1,8):
            if chessboard[king_row][n] == rook or chessboard[king_row][n] == queen:
                return True
            elif chessboard[king_row][n] != ' ':
                break
        # up vertical
        for n in range(king_row-1,-1,-1):
            if chessboard[n][king_col] == rook or chessboard[n][king_col] == queen:
                return True
            elif chessboard[n][king_col] != ' ':
                break
        # down vertical
        for n in range(king_row+1,8):
            if chessboard[n][king_col] == rook or chessboard[n][king_col] == queen:
                return True
            elif chessboard[n][king_col] != ' ':
                break
    ##### BISHOP CHECK + QUEEN
        # up and right
        count = 1
        while True:
            if king_row-count < 0 or king_col+count > 7:
                break
            print([[king_row-count],[king_col+count]])
            if chessboard[king_row-count][king_col+count] == bishop or chessboard[king_row-count][king_col+count] == queen:
                return True
            elif chessboard[king_row-count][king_col+count] != ' ':
                break
            count += 1
        # down and right
        count = 1
        while True:
            if king_row+count > 7 or king_col+count > 7:
                break
            print([[king_row+count],[king_col+count]])
            if chessboard[king_row+count][king_col+count] == bishop or chessboard[king_row+count][king_col+count] == queen:
                return True
            elif chessboard[king_row+count][king_col+count] != ' ':
                break
            count += 1
        # down and left
        count = 1
        while True:
            if king_row+count > 7 or king_col-count < 0:
                break
            print([[king_row+count],[king_col-count]])
            if chessboard[king_row+count][king_col-count] == bishop or chessboard[king_row+count][king_col-count] == queen:
                return True
            elif chessboard[king_row+count][king_col-count] != ' ':
                break
            count += 1
        # up and left
        count = 1
        while True:
            if king_row-count < 0 or king_col-count < 0:
                break
            print([[king_row-count],[king_col-count]])
            if chessboard[king_row-count][king_col-count] == bishop or chessboard[king_row-count][king_col-count] == queen:
                return True
            elif chessboard[king_row-count][king_col-count] != ' ':
                break
            count += 1
    ### CHECK NOT FOUND
        return False











#--------------------------------------------------------------------------------
    # def checkmate(board):
    #     print()

            
    # def check_square_board (board):
    #     square_board = board.split()
    #     for row in square_board:
    #         if len(row) == len(square_board):
    #             return True
    #     return False
    # print()

#-------------------------------------------------------------------------------------
# https://www.reddit.com/r/learnpython/comments/fgiqf2/codewars_is_the_king_in_check_solved_but/?tl=th

