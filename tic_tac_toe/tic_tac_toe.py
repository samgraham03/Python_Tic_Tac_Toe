# Global Variables:
# board: a 2D array containg all player piece elements
# cols
# rows

def game():
    global cols, rows
    cols, rows = (3, 3)
    global board
    board = [['*' for i in range(cols)] for j in range(rows)]
    player = 'X'
    
    while not ( won() ):
        print_board()
        move(player)

        # alternates player
        if (player == 'X'):
            player = 'O'
        else:
            player = 'X'

    print("Play Again [y/n]?")
    while ( True ):
        new_game_key = input().strip().casefold() # removes additional spaces, converts input to lowercase
        if ( new_game_key == 'y' or new_game_key == 'Y'):
            game()
        elif ( new_game_key == 'n' or new_game_key == 'N'):
            exit()
        else:
            print("INVALID")


def print_board():
    print("===")
    for i in range(cols):
        for j in range(rows):
            print(board[i][j], end='')
        print()
    print("===")


def valid_input(input, parameter):
    if not (input.strip().isdigit()): # if not a number
        return False
    elif (int(input) < 0 or int(input) >= parameter): # if not in range
        return False
    else:
        return True


def move(player):
    print("Enter move for player", player)

    print("Column: ", end = '')
    col = input()
    while not ( valid_input(col, cols) ):
        print("INVALID")
        print("Column: ", end = '')
        col = input()
    col = int(col)

    print("Row: ", end = '')
    row = input()
    while not ( valid_input(row, rows) ):
        print("INVALID")
        print("Row: ", end = '')
        row = input()
    row = int(row)

    if (board[row][col] == 'X' or board[row][col] == 'O'):
        print("Move already taken")
        move(player) # Recursion
    else:
        board[row][col] = player


def horizontal_win():
    x_streak = 0
    o_streak = 0
    for i in range(cols):
        for j in range(rows):
            if (board[i][j] == 'X'):
                x_streak += 1
                o_streak = 0
                if (x_streak == 3):
                    # print("Horizontal X Win")
                    return 'X'
            elif (board[i][j] == 'O'):
                x_streak = 0
                o_streak += 1
                if (o_streak == 3):
                    # print("Horizontal O Win")
                    return 'O'
            else:
                x_streak = 0
                o_streak = 0
            x_streak = 0
            o_streak = 0
    return '*'


def vertical_win():
    x_streak = 0
    o_streak = 0
    for j in range(rows):
        for i in range(cols):
            if (board[i][j] == 'X'):
                x_streak += 1
                o_streak = 0
                if (x_streak == 3):
                    # print("Vertical X Win")
                    return 'X'
            elif (board[i][j] == 'O'):
                x_streak = 0
                o_streak += 1
                if (o_streak == 3):
                    # print("Vertical O Win")
                    return 'O'
            else:
                x_streak = 0
                o_streak = 0
        x_streak = 0
        o_streak = 0
    return '*'


# Placeholder until modular board size is implemented
def diagonal_win():
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        # print("Diagonal X Win 1")
        return 'X'
    elif (board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X'):
        # print("Diagonal X Win 2")
        return 'X'
    elif (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        # print("Diagonal O Win 1")
        return 'O'
    elif (board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O'):
        # print("Diagonal O Win 2")
        return 'O'
    else:
        return '*'


def full_board():
    for i in range(cols):
        for j in range(rows):
            if (board[i][j] == '*'):
                return False
    return True


def won():
    if ( horizontal_win() == 'X' or vertical_win() == 'X' or diagonal_win() == 'X'):
        print_board()
        print("X won!")
        return True
    elif ( horizontal_win() == 'O' or vertical_win() == 'O' or diagonal_win() == 'O'):
        print_board()
        print("O won!")
        return True
    elif (full_board()):
        print_board()
        print("Tie Game!")
        return True
    else:
        return False


if __name__ == "__main__": # if this file is run directly:
    game()