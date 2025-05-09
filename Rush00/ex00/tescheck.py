def check_pawn(board, king_row, king_col):
    # Pawn Attack
    directions = [(-1, -1), (-1, 1)]
    for dr, dc in directions:
        row = king_row - dr
        col = king_col - dc
        # print(f"check1 {row} : {col} : {len(board)}")
        # print(board[row][col])
        if 0 <= row < len(board) and 0 <= col < len(board):
            if board[row][col] == "P":
                #print("P",row, col)
                return True
    return False
    

def check_bishop(board, king_row, king_col):
    # Bishop Attack
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    #print("K",king_row, king_col)
    for dr, dc in directions:
        row = king_row + dr
        col = king_col - dc
        #print(f"check1 {row} : {col} : {len(board)}")
        
        while 0 <= row < len(board) and 0 <= col < len(board):
            piece = board[row][col]
            if piece == "B":
                #print("B",row, col)
                return True
            elif piece != ".":
                break
            row += dr
            col -= dc
    return False

def check_rook(board, king_row, king_col):
    # Rook Attack
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #print("K",king_row, king_col)
    for dr, dc in directions:
        row = king_row + dr
        col = king_col + dc
        while 0 <= row < len(board) and 0 <= col < len(board):
            piece = board[row][col]
            if piece == "R":
                return True
            elif piece != ".":
                break
            row += dr
            col += dc
    return False

def check_queen(board, king_row, king_col):
    #print("K",king_row, king_col)
    # Queen Attack = Rook + Bishop
    return check_bishop(board, king_row, king_col) or check_rook(board, king_row, king_col)

def checkmate(board):
    board = board.split()
    #print(board)

    # Find king position
    king_row = king_col = -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "K":
                king_row = i
                king_col = j
                break
        if king_row != -1:
            break

    if (
        check_pawn(board, king_row, king_col) or
        check_bishop(board, king_row, king_col) or
        check_rook(board, king_row, king_col) or
        check_queen(board, king_row, king_col)
    ):
        print("Success")
    else:
     print("Fail!!!")








    #  Not found king display "Fail"
    # if king_row == -1:
    #     print("Fail")
    #     return

    # # Check King by attacked
    # if (
    #     check_queen(board, king_row, king_col)
    # ):
    #     print("Success")
    # else:
    #     print("Fail!!!")




