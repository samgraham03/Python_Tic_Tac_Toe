class GameBoard:    
    conects_to_win = 3
    
    def __init__(self, columns = 3, rows = 3):
        self.columns = columns
        self.rows = rows
        self.board = [['*' for i in range(columns)] for j in range(rows)] # creates a 2D array game board
    
    def get_board(self):
        return self.board

    def print_board(self):
        def print_bar():
            for i in range(2*self.columns - 1):
                print('=', sep = '', end = '')
            print()

        print_bar()
        print('\n'.join(' '.join(str(i) for i in rows) for rows in self.board))
        print_bar()

    # Needs Error Catch
    def get_dim(self, axis):
        if (axis == 'x'):
            return self.columns
        if (axis == 'y'):
            return self.rows
    
    def set_board_value(self, move, symbol):
        self.board[move[1]][move[0]] = symbol

    def get_board_value(self, move):
        return self.board[move[1]][move[0]]

    def won(self, symbol):
        def horizontal_win():
            streak = 0
            for j in range(self.rows):
                for i in range(self.columns):
                    if (self.board[j][i] == symbol):
                        streak += 1
                        if (streak == self.conects_to_win):
                            return True
                    else:
                        streak = 0
                streak = 0
            return False

        def vertical_win():
            streak = 0
            for i in range(self.columns):
                for j in range(self.rows):
                    if (self.board[j][i] == symbol):
                        streak += 1
                        if (streak == self.conects_to_win):
                            return True
                    else:
                        streak = 0
                streak = 0
            return False

        # place holder (Only works for standard sized boards)
        def diagonal_win():
            if ( self.board[0][0] == symbol and self.board[1][1] == symbol and self.board[2][2] == symbol ):
                return True
            elif ( self.board[2][0] == symbol and self.board[1][1] == symbol and self.board[0][2] == symbol ):
                return True
            else:
                return False
        
        def full_board():
            for i in range(self.columns):
                for j in range(self.rows):
                    if (self.board[j][i] == '*'):
                        return False
            return True

        if ( horizontal_win() or vertical_win() or diagonal_win() ):
            self.print_board()
            print("Player", symbol, "wins!")
            return True
        elif ( full_board() ):
            print("Tie game!")
        else:
            return False


