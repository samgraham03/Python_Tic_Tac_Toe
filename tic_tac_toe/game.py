from user_interface import UserInterface
from game_board import GameBoard
from player_piece import PlayerPiece
from player_piece import AiPlayer

def game():
    Board = GameBoard()
    UI = UserInterface()

    # UI.set_num_players()
    # print("Number of players:", UI.get_num_players()) # test code

    if (UI.get_num_players() != 2):
        print("UNIMPLEMENTED")
        exit()
    else:
        PlayerOne = PlayerPiece('X')
        PlayerTwo = PlayerPiece('O')

    players = [PlayerOne, PlayerTwo]
    
    Player = players[UI.get_turn()]
    while not (Board.won(Player.get_symbol())):
        Board.print_board()
        Player = players[UI.get_turn()]

        # Move:
        taken = True
        while (taken):
            move = Player.move( Board.get_dim('x'), Board.get_dim('y'), Player.get_symbol() )
            if (Board.get_board_value(move) == '*'):
                Board.set_board_value(move, Player.get_symbol())
                taken = False
            else:
                print("INVALID")

        UI.end_turn()
    if (UI.play_again()):
        game()
    else:
        exit()

if __name__ == "__main__":
    game()