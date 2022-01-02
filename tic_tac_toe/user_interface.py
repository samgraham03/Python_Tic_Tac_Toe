class UserInterface:
    num_players = 2
    max_num_players = 2 # To be updated in future release
    num_bots = 0
    round = 0
    turn = 0

    def __init__(self):
        pass

    def set_num_players(self):
        num_players = input("Enter number of human players: ")
        while not ( num_players.strip().isdigit() and (int(num_players.strip()) in range(1,self.max_num_players + 1)) ):
            print("INVALID")
            num_players = input("Enter number of human players: ")
        self.num_players = int(num_players.strip())

    def get_num_players(self):
        return self.num_players

    def get_turn(self):
        self.turn = self.round%(self.num_players + self.num_bots)
        return self.turn

    def end_turn(self):
        self.round += 1

    def play_again(self):
        while (True):
            new_game_key = input("Play again? [y/n]: ").strip().casefold()
            if (new_game_key == 'y'):
                return True
            elif (new_game_key == 'n'):
                return False
            else:
                print("INVALID")
