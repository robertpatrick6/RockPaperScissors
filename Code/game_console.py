# Author: Robert Patrick
#
# This script will run a rock, paper, scissors game in the console
# using the provided class


from cpu_player import CPUPlayer


MOVES = ["rock","paper","scissors"]


class ConsoleGame:

    # Constructor
    # --------------------
    # Creates a new cpu player and its internals
    def __init__(self, opponent):
        player_wins = 0
        cpu_wins = 0
        draws = 0

        player_move = ""

        print("Beginning game of Rock, Paper, Scissors...")
        print("Enter 'q' or 'quit' to exit")
        print("--------------------------------------------------\n")
        while(True):
            player_move = self.get_move().lower()

            if (player_move == "q" and player_move == "quit"):
                break

            elif (player_last_move in MOVES):
                cpu_move = opponent.make_move()

                if (player_move == cpu_move):
                    print("CPU threw {}. This round was a draw.\n".format(cpu_move))
                    draws += 1

                elif ((player_move=="rock" and cpu_move=="scissors") or
                      (player_move=="paper" and cpu_move=="rock") or
                      (player_move=="scissors" and cpu_move=="paper")):
                    print("CPU threw {}. You win this round.\n".format(cpu_move))
                    player_wins += 1

                else:
                    print("CPU threw {}. You lose this round.\n".format(cpu_move))
                    cpu_wins += 1

        print("Good game.\nYour wins: {}\nCPU wins: {}\nDraws: {}".format(player_wins,
                                                                          cpu_wins,
                                                                          draws))


    # Public methods
    # --------------------
    # This method gets a move from the player as console input
    # (This method is fairly unnecessary as is...)
    def get_move(self):
        return input("Enter your move: ")


if __name__ == "__main__":
    opponent = CPUPlayer()

    ConsoleGame(opponent)
