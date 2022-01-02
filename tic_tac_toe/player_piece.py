class PlayerPiece:
    ai_status = False

    def __init__(self, symbol = 'X'):
        self.symbol = symbol
        pass

    def move(self, columns, rows, symbol):
        move_coords = [0,0]
        print("Enter move for player", symbol)
        def valid_coord(value, max):
            coord = input(value + ": ")
            while not ( coord.strip().isdigit() and (int(coord.strip()) in range(max)) ):
                print("INVALID")
                coord = input(value + ": ")
            return int(coord.strip())
        
        move_coords[0] = valid_coord("Column", columns)
        move_coords[1] = valid_coord("Row", rows)
                
        return move_coords

    def get_symbol(self):
        return self.symbol


class AiPlayer(PlayerPiece): # inherits from PlayerPiece
    ai_status = True

    def move(self): # overrides move()
        pass