def gamestate(board):
    x_win = False
    o_win = False
    o_count = 0
    x_count = 0
    for row in board:
        x_row = 0
        o_row = 0
        for cell in row:
            if cell == "X":
                x_row += 1
                x_count += 1
            if cell == "O":
                o_row += 1
                o_count += 1
            if x_row == 3:
                x_win = True
            if o_row == 3:
                o_win = True
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count > o_count+1:
        raise ValueError("Wrong turn order: X went twice")

    diagonal = board[0][0] + board[1][1] + board[2][2]
    reverse_diagonal = board[2][0] + board[1][1] + board[0][2]
    col_0 = board[0][0] + board[1][0] + board[2][0]
    col_1 = board[0][1] + board[1][1] + board[2][1]
    col_2 = board[0][2] + board[1][2] + board[2][2]
    other_wins = [diagonal, reverse_diagonal, col_0, col_1, col_2]
    if "XXX" in other_wins:
        x_win = True
    if "OOO" in other_wins:
        o_win = True
    if x_win and o_win:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if not x_win and not o_win:
        if o_count + x_count == 9:
            return "draw"
        return "ongoing"
    
    return "win"