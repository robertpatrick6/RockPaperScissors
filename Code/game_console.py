# Author: Robert Patrick
#
# This script will run a rock, paper, scissors game in the console
# using the provided class


from cpu_player import CPUPlayer


MOVES = ["rock","paper","scissors"]
MOVES_ABBREV = ["r","p","s"]


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
        print("--------------------------------------------------")
        while(True):
            player_move = self.get_move().lower()

            # Update player move if players used an abbreviation
            if (player_move in MOVES_ABBREV):
                if (player_move == "r"):
                    player_move = "rock"
                elif (player_move == "p"):
                    player_move = "paper"
                else:
                    player_move = "scissors"

            # Quit game if player is inputs quit command
            if (player_move == "q" or player_move == "quit"):
                break

            # If player has input a move, simulate a round
            elif (player_move in MOVES):
                cpu_move = opponent.make_move()

                if (player_move == cpu_move):
                    print("CPU threw {}. This round was a draw.".format(cpu_move))
                    draws += 1

                elif ((player_move=="rock" and cpu_move=="scissors") or
                      (player_move=="paper" and cpu_move=="rock") or
                      (player_move=="scissors" and cpu_move=="paper")):
                    print("CPU threw {}. You win this round.".format(cpu_move))
                    player_wins += 1

                else:
                    print("CPU threw {}. You lose this round.".format(cpu_move))
                    cpu_wins += 1

                opponent.remember_moves(player_move)

            # Otherwise, output an error prompt
            else:
                print("Sorry, that is an invalid input. Please try again.")

        # Once game is over, output the end results
        print("\n\nGood game.\nYour wins: {}\nCPU wins: {}\nDraws: {}".format(player_wins,
                                                                              cpu_wins,
                                                                              draws))
        print("Please come play again sometime")


    # Public methods
    # --------------------
    # This method gets a move from the player as console input
    # (This method is fairly unnecessary as is...)
    def get_move(self):
        return input("\nEnter your move: ")


if __name__ == "__main__":
    opponent = CPUPlayer()

    ConsoleGame(opponent)
